from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "cd2b7c41efd5f6abc44b971805709770"

userpass = "mysql+pymysql://root:@"
basedir = "127.0.0.1"
dbname = "/crud_py"

app.config['SQLALCHEMY_DATABASE_URI'] = userpass + basedir + dbname
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    celular = db.Column(db.String(255), nullable=False)
    cep = db.Column(db.String(255), nullable=False)
    uf = db.Column(db.String(255), nullable=False)
    cidade = db.Column(db.String(255), nullable=False)
    bairro = db.Column(db.String(255), nullable=False)
    endereco = db.Column(db.String(255), nullable=False)
    numero = db.Column(db.String(255), nullable=False)

    def __init__(self,nome, email,celular,cep,uf,cidade,bairro,endereco,numero ):
        self.nome = nome
        self.email = email
        self.celular = celular
        self.cep = cep
        self.uf = uf
        self.cidade = cidade
        self.bairro = bairro
        self.endereco = endereco
        self.numero = numero

@app.route('/')
def index():
    data_cliente = db.session.query(Cliente)
    return render_template('index.html', data=data_cliente)

@app.route('/input', methods=['GET', 'POST'])
def input_data():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        celular = request.form['celular']
        cep = request.form['cep']
        uf = request.form['uf']
        cidade = request.form['cidade']
        bairro = request.form['bairro']
        endereco = request.form['endereco']
        numero = request.form['numero']

        add_data = Cliente(nome, email, celular, cep, uf, cidade, bairro, endereco, numero)

        db.session.add(add_data)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('input.html')

@app.route('/edit/<int:id>')
def edit_data(id):
    data_clients = Cliente.query.get(id)
    return render_template('edit.html', data=data_clients)


@app.route('/proses_edit', methods=['POST', 'GET'])
def proses_edit():
    data_clients = Cliente.query.get(request.form.get('id'))

    data_clients.nome = request.form['nome']
    data_clients.email = request.form['email']
    data_clients.celular = request.form['celular']
    data_clients.cep = request.form['cep']
    data_clients.uf = request.form['uf']
    data_clients.cidade = request.form['cidade']
    data_clients.bairro = request.form['bairro']
    data_clients.endereco = request.form['endereco']
    data_clients.numero = request.form['numero']

    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
    data_clientes = Cliente.query.get(id)
    db.session.delete(data_clientes)
    db.session.commit()

    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)