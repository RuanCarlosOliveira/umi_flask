from flask import Flask
from routes import init_routes

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Substitua por uma chave secreta mais segura

# Inicializando as rotas
init_routes(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
