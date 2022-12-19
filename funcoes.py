from onibus import *
from funcionario_cobrador import *
from funcionario_motorista import *


def media(lista, string):
    soma = 0
    for num in lista:                            #soma todos os valores da lista
        soma += num
    print(f'Media {string}: {soma/len(lista)}')  #retorna a soma dividida pelo comprimento da lista


def verifica_idade():
    idade = 0
    while idade > 80 or idade < 20:                             #verifica se a idade se encaixa no intervalo indicado
        idade = int(input('Informe a idade [20 a 80]: '))
        if idade > 80 or idade < 20:
            print('Erro! Informe um valor no formato indicado.')
    return idade


def verifica_funcao():
    funcao = ''
    while funcao != 'cobrador' and funcao != 'motorista':                      #verifica se a função selecionada é válida
        funcao = input('Informe a funcao [cobrador|motorista]: ').lower()
        if funcao != 'cobrador' and funcao != 'motorista':
            print('Erro! Informe uma funcao valida.')
    return funcao


def verifica_id(funcao, ids_em_uso):
    id = ''
    if funcao == 'motorista':                                                       #para as funções determinadas, verifica se o id é do formato
        while len(id) != 2 or id in ids_em_uso or id_nao_int(id):                   #certo para a função, se já está em uso e se é composto de números
            id = input(
                "Informe o id: [4 numeros = cobrador| 2 numeros = motorista] ")
            if len(id) != 2 or id_nao_int(id):
                print('Erro! Informe o id no formato especificado.')
            if id in ids_em_uso:
                print('Erro! O id digitado ja esta em uso.')
    else:
        while len(id) != 4 or id in ids_em_uso or id_nao_int(id):
            id = input(
                "Informe o id: [4 numeros = cobrador| 2 numeros = motorista] ")
            if len(id) != 4 or id_nao_int(id):
                print('Erro! Informe o id no formato especificado.')
            if id in ids_em_uso:
                print('Erro! O id digitado ja esta em uso.')
    return id


def verifica_id_em_uso(ids_em_uso, funcionarios_em_atividade):
    id = ''
    while id not in ids_em_uso or id in funcionarios_em_atividade:  #verifica se o id informado existe e se está em atividade no momento
        id = input("Informe o id: ")                                #Este é importante para que as atualizações e exclusões não ocorram,
        if id not in ids_em_uso:                                    #caso o funcionário esteja em viagem
            print('Erro! O id informado não existe.')
        if id in funcionarios_em_atividade:
            print('Erro! o funcionario esta atuando no momento.')
    return id


def verifica_salario():
    salario = 0
    while salario < 2500 or salario > 15000:                            #verifica se o salário está no intervalo especificado
        salario = float(input('Informe o salario [2500 a 15000]: '))
        if salario < 2500 or salario > 15000:
            print('Erro! O salario esta fora do intervalo aceito.')
    return salario


def consultar_destinos(destinos):
    for destino in destinos:        #mostra os destinos da lista de destinos
        print(destino)


def adicionar_destino(destinos):
    destino = input('Informe um novo destino: ').lower()
    while destino in destinos:                                  #verifica se o destino informado já está cadastrado
        print('Erro! O destino informado ja esta cadastrado.')
        destino = input('Informe um novo destino: ').lower()
    return destino


def remover_destino(destinos):
    destino = ''
    while destino not in destinos:                                      #verifica se o destino informado existe, para que possa ser excluído
        destino = input('Informe o destino a ser deletado: ').lower()
        if destino not in destinos:
            print('Erro! O destino informado nao existe.')
    return destino


def verifica_numeracao(numeracoes_em_uso):
    numero = ''
    while len(numero) != 4 or numero in numeracoes_em_uso or id_nao_int(numero):    #verifica se a numeração tem o comprimento certo, se já está em uso
        numero = input('Informe a numeracao do onibus [quatro numeros]: ')          #e se é composta por números
        if len(numero) != 4:
            print('Erro! a numeracao deve conter quatro digitos.')
        if numero in numeracoes_em_uso:
            print('Erro! O numero digitado ja esta em uso.')
        if id_nao_int(numero):
            print('Erro! Apenas numeros devem ser digitados.')
    return numero


def verifica_numeracao_em_uso(numeracoes_em_uso):
    numero = ''
    while numero not in numeracoes_em_uso:      #verifica se a numeração informada existe
        numero = input('Informe o numero: ')
        if numero not in numeracoes_em_uso:
            print('Erro! Nao existe onibus com essa numeracao.')
    return numero


def verifica_numeracao_em_uso_deletar(numeracoes_em_uso, onibus_em_atividade):
    numero = ''
    while numero not in numeracoes_em_uso or numero in onibus_em_atividade: #verifica se o número não existe e se é de um ônibus em atividade  
        numero = input('Informe o numero: ')
        if numero not in numeracoes_em_uso:
            print('Erro! Nao existe onibus com essa numeracao.')
        if numero in onibus_em_atividade:
            print('Erro! O onibus esta atuando no momento.')
    return numero


def verifica_destino(destinos, onibus_em_atividade, n):
    destino = ''
    if n in onibus_em_atividade:        #caso a numeração seja de um ônibus em atividade, verifica se a entrada não é retornou
        while destino != 'retornou':
            destino = input(
                'Informe o destino ou informe retornou caso tenha retornado: ').lower()
            if destino != 'retornou':
                print(
                    'Erro! O onibus ja esta em viagem. Assim, so eh possivel retornar.')
    else:                               #caso contrário, verifica se o destino está na lista de destinos
        while destino not in destinos:
            destino = input(
                'Informe o destino ou informe retornou caso tenha retornado: ').lower()
            if destino not in destinos:
                print('Erro! Informe um destino existente.')
            if destino == 'retornou':
                print('Observacao: O onibus ja nao esta em viagem')
    return destino


def verifica_funcionarios_atuando(funcionarios_em_atividade):
    id1 = ''
    id2 = ''            #verifica se os ids digitados têm comprimento 4 e 2
    while len(id1) != 4 and len(id1) != 2 or len(id2) != 4 and len(id2) != 2 or len(id1) == len(id2) or id1 in funcionarios_em_atividade or id2 in funcionarios_em_atividade:
        id1, id2 = input(
            'Informe os IDs dos funcionarios separados por espaço [obs: eh necessario haver um motorista e um cobrador]: ').split()
        if len(id1) != 4 and len(id1) != 2 or len(id2) != 4 and len(id2) != 2 or len(id1) == len(id2):
            print('Erro! Escreva no formato especificado.')
        if id1 in funcionarios_em_atividade or id2 in funcionarios_em_atividade:
            print('Erro! Um dos ids informados ja esta em viagem.')
    return id1, id2


def id_nao_int(id):
    #verifica se a string é composta por números
    valores_possiveis = ['0','1', '2', '3','4','5','6','7','8','9']
    for valor in id:
        if valor in valores_possiveis:
            return False
        else:
            return True


def informacoes_final_expediente(lista_onibus, lista_funcionarios):
    #retorna informações do final do expediente
    quantidade_viagens_por_funcionario(lista_funcionarios)
    ainda_nao_retornou(lista_onibus)


def quantidade_viagens_por_funcionario(lista_funcionarios):
    print()
    for funcionario in lista_funcionarios:  #para cada funcionário, mostra o id e a quantidade de viagens realizadas
        if funcionario.get_funcao() == 'cobrador':
            print(
                f'Funcionario: {funcionario.get_id_cobrador()}. Viagens realizadas: {funcionario.get_cont_viagens()}')
        else:
            print(
                f'Funcionario: {funcionario.get_id_motorista()}. Viagens realizadas: {funcionario.get_cont_viagens()}')


def ainda_nao_retornou(lista_onibus):
    cont = 0
    print('\nTodos retornaram?\n')
    for onibus in lista_onibus:         #verifica se os ônibus retornaram. Caso algum ônibus não tenha retornado, mostra os dados do veículo
        if onibus.get_status():
            print(f'Onibus: {onibus.get_numeracao()}')
            print(f'Funcionarios: {onibus.get_funcionarios_atuando()}')
            print(f'Destino: {onibus.get_destino()}')
            cont += 1
    if cont > 0:
        print('Nao retornaram, devido uma fila inesperada.\n')
    else:
        print('Todos retornaram.')


def funcionarios_disponiveis(funcionarios_em_atividade, ids_em_uso):
    cont_cobrador_disponivel = 0  #quantidade de cobrador disponível
    cont_motorista_disponivel = 0 #quantidade de motorista disponível
    for funcionario in ids_em_uso:    #verifica se há funcionários suficientes para operar um ônibus, analisando os que não estão em atividade
        if funcionario not in funcionarios_em_atividade:
            if len(funcionario) == 4:                       
                cont_cobrador_disponivel += 1
            else:
                cont_motorista_disponivel += 1

    if cont_cobrador_disponivel > 0 and cont_motorista_disponivel > 0: #se há um ou mais motoristas e um ou mais cobradores, então há funcionários suficientes
        return True
    else:
        return False


def funcionario_disponivel(funcionarios_em_atividade, ids_em_uso):
    cont = 0
    for funcionario in ids_em_uso:                          #verifica se há funcionários que não estão em viagem
        if funcionario not in funcionarios_em_atividade:
            cont += 1
    if cont > 0:
        return True
    else:
        return False
