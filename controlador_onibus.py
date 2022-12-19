from onibus import Onibus


class Controlador_onibus:
    
    def __init__(self, veiculos=[]):
        self._veiculos_ = veiculos[:]       #atributo _veículos_ receberá a lista de objetos do tipo ônibus

    def inserir(self, veiculo):
        self._veiculos_.append(veiculo)     #adiciona veiculo à lista


    def atualizar_destino(self, numero, destino):   #atualiza o destino do ônibus, dada a numeração
        for veiculo in self._veiculos_:
            if veiculo.get_numeracao() == numero:
                veiculo.set_destino(destino)
                if destino == 'nenhum' or destino == 'retornou':    #se o ônibus retornou o status fica falso
                    veiculo.set_status(False)
                else:
                    veiculo.set_status(True)                        #caso contrário, verdadeiro

    def atualizar_funcionarios_atuando(self, numero, func1, func2): #atualiza os funcionários que estão atuando, 
        for veiculo in self._veiculos_:                             #dada a numeração do ônibus
            if veiculo.get_numeracao() == numero:
                veiculo.set_funcionarios_atuando(func1, func2)

    def get_lista_funcionarios_atuando(self, numero):               #retorna a lista de funcionários atuando, dada a numeração do ônibus
        for veiculo in self._veiculos_:
            if veiculo.get_numeracao() == numero:
                return veiculo.get_funcionarios_atuando()

    def consultar(self):                                            #retorna a lista
        return self._veiculos_[:]

    def tamanho_lista_onibus(self):                                 #retorna a quantidade de ônibus do terminal
        return len(self._veiculos_)

    def deletar(self, numero):                                      #deleta o ônibus, dada a numeração do mesmo
        for veiculo in self._veiculos_:
            if veiculo.get_numeracao() == numero:
                self._veiculos_.remove(veiculo)
