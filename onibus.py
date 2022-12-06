class Onibus:
   
    def __init__(self, numeracao, destino):
        self.numeracao = numeracao
        self.destino = destino
    
    def get_destino(self):
        return self.destino
    
    def set_destino(self, destino):
        self.destino = destino
    
    def get_numeracao(self):
        return self.numeracao
    
    def set_numeracao(self, destino):
        self.numeracao = numeracao
    
    def __str__(self):
        if self.destino == '':
            return f'Onibus: {self.numeracao}, destino: nenhum'
        else:
            return f'Onibus: {self.numeracao}, destino: {self.destino}'
