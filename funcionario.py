class Funcionario:
   
    def __init__(self,nome,funcao):
        self.nome = nome
        self.funcao = funcao
    
    def get_nome(self):
        return self.nome
    
    def get_funcao(self):
        return self.funcao

    def set_nome(self,nome):
        self.nome = nome
    
    def set_funcao(self,funcao):
        self.funcao = funcao
    
    def __str__(self):
        return f'Funcionario: {self.nome}, Funcao: {self.funcao}'