from wtforms import Form, BooleanField, StringField, PasswordField, validators, IntegerField

class RegistrationForm(Form):
    nome = StringField('Nome Completo:', [validators.Length(min=4, max=25)])
    cpf = IntegerField('CPF:')
    endereco = StringField('Endereço:')
    telefone = IntegerField('Telefone:')
    email = StringField('Email:', [validators.Length(min=6, max=35), validators.Email()])
    senha = PasswordField('Nova Senha:', [
        validators.DataRequired(),
        validators.EqualTo('confirmacao', message='As senhas não combinam')
    ])
    confirmacao = PasswordField('Confirme sua Senha:')

class LoginFormulario(Form):
    email = StringField('Email:', [validators.Length(min=6, max=35), validators.Email()])
    senha = PasswordField('Senha:', [validators.DataRequired()])


