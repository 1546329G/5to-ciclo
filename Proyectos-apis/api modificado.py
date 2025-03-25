from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from models import db, User, Alumnos, Accesos, Configuracion, Invitados, Vigilante  # Importar los modelos
from dotenv import load_dotenv
import os

# Cargar las variables del archivo .env
load_dotenv()

app = Flask(__name__)

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://userlogin:S3nati123@localhost/u911718531_moviles20251'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Desactivar el rastreo de modificaciones para ahorrar memoria
app.config['JWT_SECRET_KEY'] = 'rootgS3nati123'  # Cambiar esto por una clave más segura

# Inicializamos la base de datos y JWT
db.init_app(app)
jwt = JWTManager(app)

# Crear las tablas si no existen
with app.app_context():
    db.create_all()  # Crea las tablas en la base de datos

# Ruta para registrar usuarios
@app.route('/register', methods=['POST'])
def register():
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    # Verificar si el nombre de usuario ya existe
    user = User.query.filter_by(username=username).first()
    if user:
        return jsonify({"msg": "El usuario ya existe"}), 400

    # Encriptar la contraseña
    hashed_password = generate_password_hash(password)

    # Crear un nuevo usuario
    new_user = User(username=username, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"msg": "Usuario creado exitosamente"}), 201

# Ruta de inicio de sesión (login)
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    user = User.query.filter_by(username=username).first()
    if not user or not check_password_hash(user.password, password):
        return jsonify({"msg": "Credenciales incorrectas"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)

# Ruta protegida
@app.route('/protected', methods=['POST'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

# Otras rutas adicionales para interactuar con las tablas

# Ruta para obtener todos los alumnos
@app.route('/alumnos', methods=['GET'])
@jwt_required()
def get_alumnos():
    alumnos = Alumnos.query.all()
    return jsonify([{
        "id": alumno.id,
        "dni": alumno.dni,
        "nombre": alumno.nombre,
        "programa_estudios": alumno.programa_estudios,
        "estado": alumno.estado,
        "observaciones": alumno.observaciones,
    } for alumno in alumnos])

# Ruta para obtener accesos
@app.route('/accesos', methods=['GET'])
@jwt_required()
def get_accesos():
    accesos = Accesos.query.all()
    return jsonify([{
        "id": acceso.id,
        "dni": acceso.dni,
        "fecha_hora": acceso.fecha_hora,
        "estado_acceso": acceso.estado_acceso,
        "observaciones": acceso.observaciones,
    } for acceso in accesos])

# Ruta para obtener la configuración
@app.route('/configuracion', methods=['GET'])
@jwt_required()
def get_configuracion():
    configuracion = Configuracion.query.first()
    return jsonify({
        "id": configuracion.id,
        "tiempo_caducidad": configuracion.tiempo_caducidad,
    })

# Ruta para obtener los invitados
@app.route('/invitados', methods=['GET'])
@jwt_required()
def get_invitados():
    invitados = Invitados.query.all()
    return jsonify([{
        "id": invitado.id,
        "nombre": invitado.nombre,
        "apellido": invitado.apellido,
        "created_at": invitado.created_at,
    } for invitado in invitados])

# Ruta para obtener los vigilantes
@app.route('/vigilantes', methods=['GET'])
@jwt_required()
def get_vigilantes():
    vigilantes = Vigilante.query.all()
    return jsonify([{
        "id": vigilante.id,
        "dni": vigilante.dni,
        "nombre": vigilante.nombre,
        "password": vigilante.password,
    } for vigilante in vigilantes])

if __name__ == '__main__':
    app.run(debug=True)














































from flask_sqlalchemy import SQLAlchemy

# Crear una instancia de SQLAlchemy
db = SQLAlchemy()

# Modelo para la tabla 'alumnos'
class Alumnos(db.Model):
    __tablename__ = 'alumnos'

    id = db.Column(db.Integer, primary_key=True)
    dni = db.Column(db.String(10), unique=True, nullable=False)
    nombre = db.Column(db.String(255), nullable=False)
    programa_estudios = db.Column(db.String(255), nullable=False)
    estado = db.Column(db.Enum('A', 'D', name='estado_enum'), nullable=False)
    observaciones = db.Column(db.Text, nullable=True)
    password = db.Column(db.String(50), nullable=True)

    def __repr__(self):
        return f"<Alumnos {self.nombre}>"

# Modelo para la tabla 'accesos'
class Accesos(db.Model):
    __tablename__ = 'accesos'

    id = db.Column(db.Integer, primary_key=True)
    dni = db.Column(db.String(10), db.ForeignKey('alumnos.dni'), nullable=False)
    fecha_hora = db.Column(db.TIMESTAMP, default=db.func.current_timestamp(), nullable=False)
    estado_acceso = db.Column(db.Enum('PERMITIDO', 'DENEGADO', name='estado_acceso_enum'), nullable=False)
    observaciones = db.Column(db.Text, nullable=True)
    qr_creado = db.Column(db.TIMESTAMP, default=db.func.current_timestamp(), nullable=False)
    qr_expira = db.Column(db.TIMESTAMP, nullable=False)

    alumno = db.relationship('Alumnos', backref=db.backref('accesos', lazy=True))

    def __repr__(self):
        return f"<Accesos {self.dni}>"

# Modelo para la tabla 'configuracion'
class Configuracion(db.Model):
    __tablename__ = 'configuracion'

    id = db.Column(db.Integer, primary_key=True)
    tiempo_caducidad = db.Column(db.Integer, nullable=False, default=3)

    def __repr__(self):
        return f"<Configuracion {self.tiempo_caducidad}>"

# Modelo para la tabla 'invitados'
class Invitados(db.Model):
    __tablename__ = 'invitados'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.TIMESTAMP, default=db.func.current_timestamp(), nullable=True)

    def __repr__(self):
        return f"<Invitados {self.nombre} {self.apellido}>"

# Modelo para la tabla 'vigilante'
class Vigilante(db.Model):
    __tablename__ = 'vigilante'

    id = db.Column(db.Integer, primary_key=True)
    dni = db.Column(db.String(10), nullable=False)
    nombre = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"<Vigilante {self.nombre}>"

# Modelo para la tabla 'User' (para autenticación)
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f"<User {self.username}>"
