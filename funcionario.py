class Funcionario:

    quantidade_viagens = 5

    def __init__(self, nome, funcao, idade, salario, status, cont_viagens, viagem_concluida):
        self.nome = nome
        self.funcao = funcao
        self.idade = idade
        self.salario = salario
        self.status = status
        self.cont_viagens = cont_viagens
        self.viagem_concluida = viagem_concluida

    def get_nome(self):
        return self.nome

    def get_funcao(self):
        return self.funcao

    def get_idade(self):
        return self.idade

    def get_salario(self):
        return self.salario

    def get_status(self):
        return self.status

    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def set_funcao(self, nova_funcao):
        self.funcao = nova_funcao

    def set_idade(self, nova_idade):
        self.idade = nova_idade

    def set_salario(self, novo_salario):
        self.salario = novo_salario

    def set_status(self, novo_status):
        self.status = novo_status
    
    def set_viagem_concluida(self, nova_viagem_concluida):
        self.viagem_concluida = nova_viagem_concluida
        self.cont_viagens += 1
        self.viagem_concluida = False

    
    def aumento_salarial(self):
        self.salario += 10 * self.cont_viagens

    def __str__(self):
        return f'Funcionario: {self.nome}, Funcao: {self.funcao}, Idade: {self.idade}, Salario: {self.salario}, Em viagem: {self.status}'
