from loja import mongo
from datetime import datetime

class Marca:
    def __init__(self, nome):
        self.nome = nome

        
class Categoria:
    def __init__(self, nome):
        self.nome = nome

class Produto:
    def __init__(self, nome, preco, estoque, descricao, marca, categoria, image1='image.jpg', image2='image.jpg', image3='image.jpg'):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
        self.descricao = descricao
        self.data = datetime.utcnow()
        self.marca = marca
        self.categoria = categoria
        self.image1 = image1
        self.image2 = image2
        self.image3 = image3

    @staticmethod
    def get_produtos():
        return mongo.db.Produto.find() 

    def save(self):
        Produto_data = {
            'NOME': self.nome,
            'PRECO': self.preco,
            'ESTOQUE': self.estoque,
            'DESCRICAO': self.descricao,
            'MARCA': self.marca,
            'CATEGORIA': self.categoria,
            'DATA': self.data,
            'image1': self.image1,
            'image2': self.image2,
            'image3': self.image3
        }
        return mongo.db.Produto.insert_one(Produto_data)

