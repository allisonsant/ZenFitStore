from flask import render_template, session, request, url_for, flash, redirect
from flask_pymongo import PyMongo
from loja.produtos.forms import AddProdutos
from loja import app, mongo, bcrypt
from .forms import RegistrationForm, LoginFormulario
from .models import Cliente
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import check_password_hash

app.config['MONGO_URI'] = 'mongodb://localhost:27017/ZenFitStore'
mongo = PyMongo(app)


@app.route('/')
def home(): 
    return render_template('admin/menu.html', title='Menu')

@app.route('/admin')
def admin(): 
    if 'email' not in session:
        flash(f'Faça login antes de acessar a área de administração sistema','success')
        return redirect(url_for('login'))
    produtos = list(mongo.db.Produtos.find())
    return render_template ('admin/index.html', title='Página do Administrador', produtos=produtos)

@app.route('/registrar', methods=['GET', 'POST'])
def registrar():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        Cliente = mongo.db.Cliente  # supondo que você tenha uma coleção 'users'
        hashed_password = bcrypt.generate_password_hash(form.senha.data).decode('utf-8')
        Cliente_data = {
            'NOME': form.nome.data,
            'CPF': form.cpf.data,
            'ENDERECO': form.endereco.data,
            'EMAIL': form.email.data,
            'TELEFONE': form.telefone.data,
            'SENHA': hashed_password  # Lembre-se de usar hashes para senhas na prática real
        }
        Cliente.insert_one(Cliente_data)
        flash(f'Obrigado {form.nome.data} registrar','success')
        return redirect(url_for('login'))  # Redireciona para a página de login após o registro
    return render_template('admin/registrar.html', form=form, title='Página de Registros')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginFormulario(request.form)
    if request.method == 'POST':
      email = request.form['email']
      senha = request.form['senha']
      if email == 'zenfitstore@gmail.com' or senha == '123456789':
          session['email'] = email
          return redirect(url_for('admin'))
      else:
          return 'Credenciais inválidas. Tente novamente.'
    return render_template('admin/login.html', form=form, title='Página de Login')


