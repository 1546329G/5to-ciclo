from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from models import db, User  # Importamos la base de datos y el modelo User
from dotenv import load_dotenv
import os

# Cargar las variables del archivo .env
load_dotenv()


app = Flask(__name__)

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://userlogin:rootgandy@localhost/userlogin'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Desactivar el rastreo de modificaciones para ahorrar memoria
app.config['JWT_SECRET_KEY'] = 'rootgandy'  # Cambiar esto por una clave más segura

# Inicializamos la base de datos y JWT
db.init_app(app)
jwt = JWTManager(app)

# Crear las tablas si no existen
with app.app_context():
    db.create_all()  # Crea las tablas en la base de datos

@app.route('/register', methods=['POST'])
def register():
    # Obtener los datos del usuario
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
@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

if __name__ == '__main__':
    app.run(debug=True)
