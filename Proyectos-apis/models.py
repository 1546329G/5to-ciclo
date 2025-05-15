from flask_sqlalchemy import SQLAlchemy

# Inicializamos la base de datos
db = SQLAlchemy()

# Definimos el modelo de Usuario
class User(db.Model):
    __tablename__ = 'users'  # Nombre de la tabla en la base de datos

    id = db.Column(db.Integer, primary_key=True)  # ID del usuario, clave primaria
    username = db.Column(db.String(80), unique=True, nullable=False)  # Nombre de usuario único
    password = db.Column(db.String(255), nullable=False)  # Contraseña del usuario (encriptada)

    def __repr__(self):
        return f'<User {self.username}>'

