from funcionario import Funcionario


class Motorista(Funcionario):
    def __init__(self, nome, funcao, idade, salario, status, cont_viagens, id_motorista):
        super().__init__(nome, funcao, idade, salario, status, cont_viagens)
        self.id_motorista = id_motorista

    def get_id_motorista(self):
        return self.id_motorista

    def set_id_motorista(self, novo_id_motorista):
        self.id_motorista = novo_id_motorista

    def aumento_salarial(self):
        self.salario += 10 * self.cont_viagens + 10

    def __str__(self):
        return super(Motorista, self).__str__() + f', ID do motorista: {self.id_motorista}'
