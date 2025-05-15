from flask import Flask
from flask_jwt_extended import JWTManager, decode_token

# Configurar la aplicación Flask
app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'tu_clave_secreta'  # Asegúrate de usar la misma clave que en tu API
jwt = JWTManager(app)  # Inicializa JWTManager con la app

def desencriptar_jwt(token):
    """Decodifica un token JWT y devuelve su contenido."""
    try:
        with app.app_context():  # Se necesita contexto para JWTManager
            decoded_data = decode_token(token)
            return decoded_data
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    token = input("Ingresa el token JWT: ").strip()  # Elimina espacios en blanco
    token = token.replace('"', '')  # Elimina comillas dobles extras
    token = token.replace("access_token: ", "").strip()  # Elimina "access_token: " si lo pegaste
    resultado = desencriptar_jwt(token)
    print(resultado)
