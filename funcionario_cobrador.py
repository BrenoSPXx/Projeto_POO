from funcionario import Funcionario


class Cobrador(Funcionario):
    def __init__(self, nome, funcao, idade, salario, status, cont_viagens, viagem_concluida, id_cobrador):
        super().__init__(nome, funcao, idade, salario, status, cont_viagens, viagem_concluida)
        self.id_cobrador = id_cobrador

    def get_id_cobrador(self):
        return self.id_cobrador

    def set_id_cobrador(self, novo_id_cobrador):
        self.id_cobrador = novo_id_cobrador
    
    def aumento_salarial(self):
        self.salario += 10 * self.cont_viagens + 5

    def __str__(self):
        return super(Cobrador, self).__str__() + f', ID do cobrador: {self.id_cobrador}'
