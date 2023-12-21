from loja import mongo

class Cliente:
    def __init__(self, nome, cpf, endereco, telefone, email, senha, profile):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
        self.senha = senha
        self.profile = profile

    @staticmethod
    def get_clientes():
        return mongo.db.Cliente.find()  # Obtém todos os clientes

    def save(self):
        Cliente_data = {
            'NOME': self.nome,
            'CPF': self.cpf,
            'ENDERECO': self.endereco,
            'TELEFONE': self.telefone,
            'EMAIL': self.email,
            'SENHA': self.senha
        }
        return mongo.db.Cliente.insert_one(Cliente_data)  # Insere o cliente na coleção 'cliente'

# Exemplo de uso:
# Cliente = Cliente('Nome do Cliente', '12345678900', 'Endereço do Cliente', 'cliente@email.com', 'senhadocliente', 'profile')
# Cliente.save()  # Salva o cliente no banco de dados

# Para recuperar todos os clientes salvos:
# Clientes = Cliente.get_clientes()
# for c in Cliente:
   # print(c)
