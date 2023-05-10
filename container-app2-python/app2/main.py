from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Cria a instância do Flask
app = Flask(__name__)

# Configurações do banco de dados SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Cria a instância do SQLAlchemy
db = SQLAlchemy(app)

# Define o modelo de dados da tabela "users"
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)

# Cria a rota para a página inicial da aplicação
@app.route('/')
def index():
    return 'Bem-vindo ao aplicativo 2!'

if __name__ == '__main__':
    # Cria as tabelas do banco de dados se elas não existirem
    db.create_all()

    # Inicia a aplicação na porta 5000
    app.run(host='0.0.0.0', port=5000, debug=True)
