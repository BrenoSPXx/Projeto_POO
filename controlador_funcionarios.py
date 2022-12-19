from funcionario_cobrador import *
from funcionario_motorista import *


class Controlador_funcionarios:

    def __init__(self, funcionarios=[]):
        self._funcionarios_ = funcionarios[:]   #atributo _funcionários_ recebrá a lista de objetos do tipo funcionário

    def inserir(self, funcionario):
        self._funcionarios_.append(funcionario) #adiciona funcionário à lista

    def atualizar_nome(self, id, nome):
        for funcionario in self._funcionarios_:             #atualiza o nome do funcionário, dado o id
            if funcionario.get_funcao() == 'cobrador':
                if funcionario.get_id_cobrador() == id:
                    funcionario.set_nome(nome)
            else:
                if funcionario.get_id_motorista() == id:
                    funcionario.set_nome(nome)

    def atualizar_idade(self, id, idade):
        for funcionario in self._funcionarios_:             #atualiza a idade do funcionário, dado o id
            if funcionario.get_funcao() == 'cobrador':
                if funcionario.get_id_cobrador() == id:
                    funcionario.set_idade(idade)
            else:
                if funcionario.get_id_motorista() == id:
                    funcionario.set_idade(idade)

    def atualizar_salario(self, id, salario):               #atualiza o salário do funcionário, dado o id
        for funcionario in self._funcionarios_:
            if funcionario.get_funcao() == 'cobrador':
                if funcionario.get_id_cobrador() == id:
                    funcionario.set_salario(salario)
            else:
                if funcionario.get_id_motorista() == id:
                    funcionario.set_salario(salario)

    def atualizar_status(self, id, status):                 #atualiza o status do funcionário, dado o id
        for funcionario in self._funcionarios_:
            if funcionario.get_funcao() == 'cobrador':
                if funcionario.get_id_cobrador() == id:
                    funcionario.set_status(status)
            else:
                if funcionario.get_id_motorista() == id:
                    funcionario.set_status(status)

    def consultar(self):                                    #retorna a lista
        return self._funcionarios_[:]

    def deletar(self, id):
        for funcionario in self._funcionarios_:             #deleta o funcionário, dado o id
            if funcionario.get_funcao() == 'cobrador':
                if funcionario.get_id_cobrador() == id:
                    self._funcionarios_.remove(funcionario)
            else:
                if funcionario.get_id_motorista() == id:
                    self._funcionarios_.remove(funcionario)

    def tamanho_lista_funcionarios(self):                  #retorna a quantidade de funcionários do terninal
        return len(self._funcionarios_)
