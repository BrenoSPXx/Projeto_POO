from funcionario_cobrador import *
from funcionario_motorista import *


class controlador_funcionarios:

    def __init__(self, funcionarios=[]):
        self._funcionarios_ = funcionarios[:]

    def inserir(self, funcionario):
        self._funcionarios_.append(funcionario)

    def atualizar_nome(self, id, nome):
        for funcionario in self._funcionarios_:
            if funcionario.get_funcao() == 'cobrador':
                if funcionario.get_id_cobrador() == id:
                    funcionario.set_nome(nome)
            else:
                if funcionario.get_id_motorista() == id:
                    funcionario.set_nome(nome)

    def atualizar_funcao(self, id, funcao):
        for funcionario in self._funcionarios_:
            if funcionario.get_funcao() == 'cobrador':
                if funcionario.get_id_cobrador() == id:
                    funcionario.set_funcao(funcao)
            else:
                if funcionario.get_id_motorista() == id:
                    funcionario.set_funcao(funcao)

    def atualizar_idade(self, id, idade):
        for funcionario in self._funcionarios_:
            if funcionario.get_funcao() == 'cobrador':
                if funcionario.get_id_cobrador() == id:
                    funcionario.set_idade(idade)
            else:
                if funcionario.get_id_motorista() == id:
                    funcionario.set_idade(idade)

    def atualizar_salario(self, id, salario):
        for funcionario in self._funcionarios_:
            if funcionario.get_funcao() == 'cobrador':
                if funcionario.get_id_cobrador() == id:
                    funcionario.set_salario(salario)
            else:
                if funcionario.get_id_motorista() == id:
                    funcionario.set_salario(salario)


    def atualizar_status(self, id, status):
        for funcionario in self._funcionarios_:
            if funcionario.get_funcao() == 'cobrador':
                if funcionario.get_id_cobrador() == id:
                    funcionario.set_status(status)
            else:
                if funcionario.get_id_motorista() == id:
                    funcionario.set_status(status)


    def consultar(self):
        return self._funcionarios_[:]


    def deletar(self, id):
        for funcionario in self._funcionarios_:
            if funcionario.get_funcao() == 'cobrador':
                if funcionario.get_id_cobrador() == id:
                    self._funcionarios_.remove(funcionario)
            else:
                if funcionario.get_id_motorista() == id:
                    self._funcionarios_.remove(funcionario)
    
    def tamanho_lista_funcionarios(self):
        return len(self._funcionarios_)

    def lista_id(self):
        lista = []
        for funcionario in self._funcionarios_:
            lista.append(funcionario.get_id())
        return lista
