from controlador_funcionarios import *
from controlador_onibus import *
from funcionario_cobrador import *
from funcionario_motorista import *
from funcoes import *

funcionarios_em_atividade = []
onibus_em_atividade = []
ids_em_uso = ['0123', '34', '0102']
numeracoes_em_uso = ['1234', '1432', '8954']
destinos = ['praia', 'centro', 'interior']


class Sistema:
    def __init__(self):
        self._controlador_1 = controlador_funcionarios([Cobrador('Roberto', 'cobrador', 30, 5000, False, 0, False, '0123'), Motorista(
            'Carlos', 'motorista', 30, 5000, False, 0, False, '34'), Cobrador('Diego', 'cobrador', 30, 5000, False, 0, False, '0102')])
        self._controlador_2 = controlador_onibus(
            [Onibus('1234', '', False, '', ''), Onibus('1432', '', False, '', ''), Onibus('8954', '', False, '', '')])
        self._rodando_ = True

    def inserir_funcionario(self):
        nome = input("Informe o nome: ")
        idade = verifica_idade()
        funcao = verifica_funcao()
        id = verifica_id(funcao, ids_em_uso)
        salario = verifica_salario()
        if len(id) == 4:
            func = Cobrador(nome, funcao, idade, salario, False, 0, False, id)
        else:
            func = Motorista(nome, funcao, idade, salario, False, 0, False, id)
        ids_em_uso.append(id)
        self._controlador_1.inserir(func)

    def atualizar_funcionario(self):
        id = verifica_id_em_uso(ids_em_uso, funcionarios_em_atividade)

        nome = input("Informe o nome: ")
        funcao = verifica_funcao()
        idade = verifica_idade()
        salario = verifica_salario()
        self._controlador_1.atualizar_nome(id, nome)
        self._controlador_1.atualizar_funcao(id, funcao)
        self._controlador_1.atualizar_idade(id, idade)
        self._controlador_1.atualizar_salario(id, salario)

    def deletar_funcionario(self):
        id = verifica_id_em_uso(ids_em_uso, funcionarios_em_atividade)
        ids_em_uso.remove(id)
        self._controlador_1.deletar(id)

    def consultar_funcionario(self):
        for funcionario in self._controlador_1.consultar():
            print(funcionario)

    def inserir_onibus(self):
        numero = verifica_numeracao(numeracoes_em_uso)
        n = Onibus(numero)
        numeracoes_em_uso.append(numero)
        self._controlador_2.inserir(n)

    def atualizar_onibus(self):

        n = verifica_numeracao_em_uso(numeracoes_em_uso)
        destino = verifica_destino(destinos, onibus_em_atividade,n)
        if destino != 'nenhum' and destino != 'retornou':
            id1, id2 = verifica_funcionarios_atuando(funcionarios_em_atividade)
            
            onibus_em_atividade.append(n)
            funcionarios_em_atividade.append(id1)
            funcionarios_em_atividade.append(id2)

            self._controlador_2.atualizar_destino(n, destino)
            self._controlador_2.atualizar_funcionarios_atuando(n, id1, id2)
            for funcionario in self._controlador_1.consultar():
                if funcionario.get_funcao() == 'motorista':
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
            self._controlador_2.atualizar_destino(n, 'retornou')
            self._controlador_2.atualizar_funcionarios_atuando(n, '', '')

            onibus_em_atividade.remove(n)
   
            for ids in self._controlador_2.get_lista_funcionarios_atuando(n):
                print(ids)
                for funcionario in self._controlador_1.consultar():
                    if len(ids) == 4 and funcionario.get_funcao() == 'cobrador':
                        if funcionario.get_id_cobrador() == ids:
                            funcionario.set_status(False)
                            funcionario.set_viagem_concluida(True)
                    elif len(ids) == 2 and funcionario.get_funcao() == 'motorista':
                        if funcionario.get_id_motorista() == ids:
                            funcionario.set_status(False)
                            funcionario.set_viagem_concluida(True)




    def deletar_onibus(self):
        n = verifica_numeracao_em_uso_deletar(numeracoes_em_uso, onibus_em_atividade)
        numeracoes_em_uso.remove(n)
        self._controlador_2.deletar(n)

    def consultar_onibus(self):
        for veiculo in self._controlador_2.consultar():
            print(veiculo)

    def consultar_estatisticas(self):
        salarios = []
        idades = []
        for funcionario in self._controlador_1.consultar():
            salarios.append(funcionario.get_salario())
            idades.append(funcionario.get_idade())
        media(salarios, 'salarios')
        media(idades, 'idades')
        print(f'Quantidade de funcionarios: {self._controlador_1.tamanho_lista_funcionarios()}')
        print(f'Quantidade de onibus: {self._controlador_2.tamanho_lista_onibus()}')
        


    def funcionando(self):
        hora = 0
        dia = 0
        cont = 0
        while self._rodando_:
            if hora == 24:
                informacoes_final_expediente(self._controlador_2.consultar(), self._controlador_1.consultar())
                dia += 1
                hora = 0
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
                cont += 1
                if cont == self._controlador_2.tamanho_lista_onibus():
                    hora += 1
                    cont = 0
            elif opcao == 7:
                self.deletar_onibus()
            elif opcao == 8:
                self.consultar_onibus()
            elif opcao == 9:
                self.consultar_estatisticas()
            elif opcao == 10:
                consultar_destinos(destinos)
            elif opcao == 11:
                destinos.append(adicionar_destino(destinos))
            elif opcao == 12:
                destinos.remove(remover_destino(destinos))
            else:
                print('Fim do programa.')
                self._rodando_ = False


Sistema().funcionando()
