"""
Aluno: Breno da Silva Pereira
Matrícula: 22203153
Turma: 01208A

Projeto aplicação: Sistema de terminal de ônibus
"""


from controlador_funcionarios import *
from controlador_onibus import *
from funcionario_cobrador import *
from funcionario_motorista import *
from funcoes import *

funcionarios_em_atividade = []                      #lista com os funcionários que estão atuando
onibus_em_atividade = []                            #lista com os onibus que estão atuando
ids_em_uso = ['0123', '34', '0102']                 #lista com os ids que estão sendo utilizadas pelos funcionários
numeracoes_em_uso = ['1234', '1432', '8954']        #lista com as numerações que estão sendo utilizadas pelos ônibus
destinos = ['praia', 'centro', 'interior']          #lista com os destinos possíveis 


class Sistema:
    def __init__(self):
        #Funcionários e veículos predefinidos:
        self._controlador_1 = Controlador_funcionarios([Cobrador('Roberto', 'cobrador', 30, 5000, False, 0, '0123'), Motorista(
            'Carlos', 'motorista', 30, 5000, False, 0, '34'), Cobrador('Diego', 'cobrador', 30, 5000, False, 0, '0102')])
        self._controlador_2 = Controlador_onibus(
            [Onibus('1234', '', False, '', ''), Onibus('1432', '', False, '', ''), Onibus('8954', '', False, '', '')])
        #Atributo que indica que o programa está operando:
        self._rodando_ = True

    def inserir_funcionario(self):
        nome = input("Informe o nome: ")
        idade = verifica_idade()                                
        funcao = verifica_funcao()
        id = verifica_id(funcao, ids_em_uso)
        salario = verifica_salario()
        if len(id) == 4:
            func = Cobrador(nome, funcao, idade, salario, False, 0, id)   #instância gerada a partir das definições do usuário
        else:
            func = Motorista(nome, funcao, idade, salario, False, 0, id)
        ids_em_uso.append(id)               #o id selecionado é armazenado na lista ids_em_uso
        self._controlador_1.inserir(func)   #a instância gerada é inserida na lista de objetos do tipo funcionario

    def atualizar_funcionario(self):
        if funcionario_disponivel(funcionarios_em_atividade, ids_em_uso):       #se o funcionário não estiver em viagem será possível atualizar
            id = verifica_id_em_uso(ids_em_uso, funcionarios_em_atividade)
            nome = input("Informe o nome: ")
            idade = verifica_idade()
            salario = verifica_salario()
            self._controlador_1.atualizar_nome(id, nome)        #para o id selecionado, os valores são atualizados
            self._controlador_1.atualizar_idade(id, idade)
            self._controlador_1.atualizar_salario(id, salario)

        else:
            print('Nao ha como atualizar ninguem! Todos estao em viagem.')

    def deletar_funcionario(self):
        if funcionario_disponivel(funcionarios_em_atividade, ids_em_uso):    #se o funcionário não estiver em viagem será possível deletar
            id = verifica_id_em_uso(ids_em_uso, funcionarios_em_atividade)
            ids_em_uso.remove(id)    #o id selecionado é removido da lista de ids em uso
            self._controlador_1.deletar(id) #o funcionário que possuí o id selecionado é deletado da lista de objetos do tipo funcionario
        else:
            print('Nao ha como remover ninguem! Todos estao em viagem.')

    def consultar_funcionario(self):
        for funcionario in self._controlador_1.consultar():
            print(funcionario)

    def inserir_onibus(self):
        numero = verifica_numeracao(numeracoes_em_uso)
        n = Onibus(numero, '', False, '', '')   #intância gerada dado o número selecionado
        numeracoes_em_uso.append(numero)        #número é armazenado na lista de numerações em uso
        self._controlador_2.inserir(n)          #a instância gerada é adionada à lista de objetos do tipo onibus

    def atualizar_onibus(self):

        n = verifica_numeracao_em_uso(numeracoes_em_uso)
        destino = verifica_destino(destinos, onibus_em_atividade, n)
        if destino != 'nenhum' and destino != 'retornou':                           #caso o destino do onibus não seja retornou
            if funcionarios_disponiveis(funcionarios_em_atividade, ids_em_uso):     #se haver funcionário suficiente para viagem
                id1, id2 = verifica_funcionarios_atuando(
                    funcionarios_em_atividade)

                onibus_em_atividade.append(n)                                       #ônibus selecionado é incluído na lista de onibus em atividade
                funcionarios_em_atividade.append(id1)                               #funcionários selecionados são incluídos na lista de funcionários em atividade
                funcionarios_em_atividade.append(id2)                               

                self._controlador_2.atualizar_destino(n, destino)                   #O destino é atualizado para o selecionado
                self._controlador_2.atualizar_funcionarios_atuando(n, id1, id2)     #Os funcionários que operam o ônibus são atualizados para os selecionados
                
                for funcionario in self._controlador_1.consultar():                 #Busca os funcionários selecionados para modificar seus status,       
                    if funcionario.get_funcao() == 'motorista':                     #indicando que estão em viagem
                        if id1 == funcionario.get_id_motorista():
                            funcionario.set_status(True)
                        elif id2 == funcionario.get_id_motorista():
                            funcionario.set_status(True)
                    else:
                        if id1 == funcionario.get_id_cobrador():
                            funcionario.set_status(True)
                        elif id2 == funcionario.get_id_cobrador():
                            funcionario.set_status(True)
            else:

                print('\nErro! Nao ha funcionarios suficientes.')

        else:                                                                       #caso o destino do ônibus seja retornou
            self._controlador_2.atualizar_destino(n, 'retornou')                    #o destino é atualizado, indicando que o ônibus não está mais em viagem
            onibus_em_atividade.remove(n)                                           #o ônibus é removido da lista de ônibus em atividade

            for ids in self._controlador_2.get_lista_funcionarios_atuando(n):       #Busca os funcionários que estavam atuando para atualizar o status para Falso,
                for funcionario in self._controlador_1.consultar():                 #indicando que não estão em viagem
                    if len(ids) == 4 and funcionario.get_funcao() == 'cobrador':
                        if funcionario.get_id_cobrador() == ids:
                            funcionario.set_status(False)
                            funcionario.set_viagem_concluida()
                            funcionarios_em_atividade.remove(ids)
                    elif len(ids) == 2 and funcionario.get_funcao() == 'motorista':
                        if funcionario.get_id_motorista() == ids:
                            funcionario.set_status(False)
                            funcionario.set_viagem_concluida()
                            funcionarios_em_atividade.remove(ids)
            self._controlador_2.atualizar_funcionarios_atuando(n, '', '')           #os funcionários atuando são atualizados para nenhum

    def deletar_onibus(self):
        n = verifica_numeracao_em_uso_deletar(
            numeracoes_em_uso, onibus_em_atividade)
        numeracoes_em_uso.remove(n)                     #Numeração é removida da lista de numerações em uso
        self._controlador_2.deletar(n)                  #O ôninus selecionado é removido da lista de objetos do tipo ônibus

    def consultar_onibus(self):
        for veiculo in self._controlador_2.consultar():
            print(veiculo)

    def consultar_estatisticas(self):
        salarios = []
        idades = []
        for funcionario in self._controlador_1.consultar(): #para cada funcionário da lista de objetos, o salário e a idade são armazenados em listas
            salarios.append(funcionario.get_salario())
            idades.append(funcionario.get_idade())
        media(salarios, 'salarios')                         #é realizada a média desses valores
        media(idades, 'idades')
        print(
            f'Quantidade de funcionarios: {self._controlador_1.tamanho_lista_funcionarios()}')      #retorna a quantidade de funcionários do terminal
        print(
            f'Quantidade de onibus: {self._controlador_2.tamanho_lista_onibus()}')                  #retorna a quantidade de ônibus do terminal

    def funcionando(self):
        hora = 0    #conta hora
        dia = 0     #conta dia
        cont = 0    #conta a quantidade de vezes que o usuário seleciona atualizar ônibus
        while self._rodando_:   #enquanto o atributo _rodando_ estiver ativo, o programa funcionará
            if hora == 24:      #terminado o expediente
                                #são mostradas as informações do dia, com quantidade de viagens de cada funcionário e se algum veículo não retornou
                informacoes_final_expediente(self._controlador_2.consultar(), self._controlador_1.consultar())
                for funcionario in self._controlador_1.consultar():         #os status e contadores de viagens são resetados
                    funcionario.set_status(False)
                    funcionario.set_cont_viagens(0)
                for onibus in self._controlador_2.consultar():
                    onibus.set_status(False)
                funcionarios_em_atividade.clear()
                onibus_em_atividade.clear()
                dia += 1 #dia incrementa
                hora = 0 #hora retorna a 0
            else:                                           #opções oferecidas pelo programa
                print()
                print('-' * 30)
                print(f'DIA: {dia} | HORÁRIO: {hora}h')
                print('-' * 30)

                print()
                print('-=' * 30)
                print('1 - Inserir funcionario')
                print('2 - Atualizar funcionario')
                print('3 - Deletar funcionario')
                print('4 - Consultar funcionario')
                print()
                print('5 - Inserir onibus')
                print('6 - Atualizar onibus')
                print('7 - Deletar onibus')
                print('8 - Consultar onibus')
                print()
                print('9 - consultar estatisticas da empresa')
                print()
                print('10 - Consultar destinos possiveis')
                print('11 - adicionar destinos')
                print('12 - deletar destinos')
                print()
                print('13 - Sair do programa')
                print('-=' * 30)
                print()

                opcao = 0                       
                while opcao < 1 or opcao > 13:
                    opcao = int(input("Informe uma opcao: "))
                    if opcao < 1 or opcao > 13:
                        print('Erro! Informe uma opcao valida')
                    print()
                                                #realiza o método de acordo com a opção selecionada:
                if opcao == 1:
                    self.inserir_funcionario()
                elif opcao == 2:
                    self.atualizar_funcionario()
                elif opcao == 3:
                    self.deletar_funcionario()
                elif opcao == 4:
                    self.consultar_funcionario()
                elif opcao == 5:
                    self.inserir_onibus()
                elif opcao == 6:
                    self.atualizar_onibus()
                    cont += 1                                                   #a cada atualização do ônibus o contador incrementa
                    if cont == self._controlador_2.tamanho_lista_onibus():      #se o contador chegar ao tamanho da lista de ônibus, a hora incrementa
                        hora += 1                                               #obs: essa lógica foi feita para fim de testes e foi a forma que eu encontrei
                        cont = 0                                                #de tornar a passagem de tempo um pouco mais coerente, visto que, dessa forma,
                elif opcao == 7:                                                #todos os veículos podem ser atualizados sem que a hora seja incrementada.
                    self.deletar_onibus()
                elif opcao == 8:
                    self.consultar_onibus()
                elif opcao == 9:
                    self.consultar_estatisticas()
                elif opcao == 10:
                    consultar_destinos(destinos)                #obs: essas funções não são métodos
                elif opcao == 11:
                    destinos.append(adicionar_destino(destinos))
                elif opcao == 12:
                    destinos.remove(remover_destino(destinos))
                else:         #caso o usuário selecione 13, o atributo _rodando_ recebe Falso, terminando a execução programa                          
                    print('Fim do programa.')
                    self._rodando_ = False


Sistema().funcionando()         #acionando o método funcionado de Sistema
