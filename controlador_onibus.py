from onibus import Onibus
from funcionario_cobrador import *
from funcionario_motorista import *


class controlador_onibus:
    def __init__(self, veiculos=[]):
        self._veiculos_ = veiculos[:]

    def inserir(self, veiculo):
        self._veiculos_.append(veiculo)

    def atualizar_numero(self, numero):
        for veiculo in self._veiculos_:
            if veiculo.get_numeracao() == numero:
                veiculo.set_numeracao(numero)

    def atualizar_destino(self, numero, destino):
        for veiculo in self._veiculos_:
            if veiculo.get_numeracao() == numero:
                veiculo.set_destino(destino)
                if destino == 'nenhum' or destino == 'retornou':
                    veiculo.set_status(False)
                else:
                    veiculo.set_status(True)

    def atualizar_funcionarios_atuando(self, numero, func1, func2):
        for veiculo in self._veiculos_:
            if veiculo.get_numeracao() == numero:
                veiculo.set_funcionarios_atuando(func1, func2)
    
    def get_lista_funcionarios_atuando(self, numero):
        for veiculo in self._veiculos_:
            if veiculo.get_numeracao() == numero:
                return veiculo.get_funcionarios_atuando()

    def consultar(self):
        return self._veiculos_[:]

    def tamanho_lista_onibus(self):
        return len(self._veiculos_)

    def deletar(self, numero):
        for veiculo in self._veiculos_:
            if veiculo.get_numeracao() == numero:
                self._veiculos_.remove(veiculo)
