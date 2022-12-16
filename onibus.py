class Onibus:
   
    def __init__(self, numeracao, destino, status, func1, func2):
        self.numeracao = numeracao
        self.destino = destino
        self.status = status
        self.func1 = func1
        self.func2 = func2
    
    def get_destino(self):
        return self.destino
    
    def get_numeracao(self):
        return self.numeracao
    
    def get_status(self):
        return self.status
    
    def set_destino(self, destino):
        self.destino = destino
    
    def set_numeracao(self, numeracao):
        self.numeracao = numeracao
    
    def set_status(self, novo_status):
        self.status = novo_status
    
    def set_funcionarios_atuando(self, func1, func2):
        self.func1 = func1
        self.func2 = func2
    
    def get_funcionarios_atuando(self):
        return [self.func1, self.func2]

    def __str__(self):
        if self.destino == '' or self.destino == 'retornou' or self.status == False:
            return f'Onibus: {self.numeracao}, destino: nenhum'
        else:
            return f'Onibus: {self.numeracao}, destino: {self.destino}, IDs dos funcionarios atuando: {self.func1}, {self.func2}'
