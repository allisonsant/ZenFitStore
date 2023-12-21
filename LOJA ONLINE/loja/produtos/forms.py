from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField, FileRequired
from wtforms import Form, IntegerField, StringField, TextAreaField, validators, FloatField

class AddProdutos(Form):
    nome = StringField('Nome: ', validators=[validators.DataRequired()])
    preco = FloatField('Preço: ', validators=[validators.DataRequired()])
    estoque = IntegerField('Estoque: ', validators=[validators.DataRequired()])
    descricao = TextAreaField('Descrição: ', validators=[validators.DataRequired()])

    image1 = FileField('1° Imagem: ', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif', 'jpeg'])])
    image2 = FileField('2° Imagem: ', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif', 'jpeg'])])
    image3 = FileField('3° Imagem: ', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif', 'jpeg'])])
