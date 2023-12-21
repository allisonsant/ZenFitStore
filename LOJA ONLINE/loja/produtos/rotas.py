from flask import redirect, render_template, url_for, flash, request
from .forms import AddProdutos
from flask_pymongo import PyMongo
from loja import app, mongo, bcrypt, photos
from .models import Marca, Categoria, Produto
import secrets

@app.route('/addmarca', methods=['GET', 'POST'])
def addmarca():
    if request.method == 'POST':
        getmarca = request.form.get('marca')
        db = mongo.db
        db.marca.insert_one({'nome': getmarca})
        flash(f'A marca {getmarca} foi cadastrada com sucesso', 'success')
        return redirect(url_for('addmarca'))
    return render_template('produtos/addmarca.html', marca='marcas')

@app.route('/addcat', methods=['GET', 'POST'])
def addcat():
    if request.method == 'POST':
        getcategoria = request.form.get('categoria')
        db = mongo.db
        db.categoria.insert_one({'nome': getcategoria})
        flash(f'A categoria {getcategoria} foi cadastrada com sucesso', 'success')
        return redirect(url_for('addcat'))
    return render_template('produtos/addmarca.html')

@app.route('/addproduto', methods=['GET', 'POST'])
def addproduto():
    marcas = list(mongo.db.marca.find())
    categorias = list(mongo.db.categoria.find())
    form = AddProdutos(request.form)

    if request.method == "POST": 
        Produto = mongo.db.Produto  # Use o nome correto da coleção aqui
        marca_selecionada = request.form.get('marca')
        categoria_selecionada = request.form.get('categoria')

        photos.save(request.files.get('image1'), name=secrets.token_hex(10)+".")
        photos.save(request.files.get('image2'), name=secrets.token_hex(10)+".")
        photos.save(request.files.get('image3'), name=secrets.token_hex(10)+".")
        Produto_data = {
            'NOME': form.nome.data,
            'PRECO': form.preco.data,
            'ESTOQUE': form.estoque.data,
            'DESCRICAO': form.descricao.data,
            'MARCA': marca_selecionada,
            'CATEGORIA': categoria_selecionada
        }
        Produto.insert_one(Produto_data)
        flash(f'Produto {form.nome.data} foi cadastrado com sucesso')
        return redirect(url_for('admin'))
    
    # Se o método HTTP não for POST ou o formulário não for válido,
    # você precisa renderizar o template novamente para exibir o formulário.
    return render_template('produtos/addproduto.html', title="Cadastrar Produtos", form=form, marcas=marcas, categorias=categorias)

from flask import request

@app.route('/consultar_produtos', methods=['GET', 'POST'])
def consultar_produtos():
    if request.method == 'POST':
        # Lógica para consultar produtos com base nos critérios do formulário
        nome = request.form.get('nome')
        preco = request.form.get('preco')
        estoque = request.form.get('estoque')

        # Implemente a lógica de consulta ao MongoDB com base nos critérios fornecidos
        # produtos = Consulta ao MongoDB com os critérios

        # Renderizar o template com os resultados da consulta
    return render_template('produtos/consultar_produtos.html')




