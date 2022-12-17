from onibus import*
from funcionario_cobrador import*
from funcionario_motorista import*

def media(lista, string):
    soma = 0
    for num in lista:
        soma += num
    print(f'Media {string}: {soma/len(lista)}')

def verifica_idade():
    idade = 0
    while idade > 80 or idade < 20:
        idade = int(input('Informe a idade [20 a 80]: '))
        if idade > 80 or idade < 20:
            print('Erro! Informe um valor no formato indicado.')
    return idade

def verifica_funcao():
    funcao = ''
    while funcao != 'cobrador' and funcao != 'motorista':
        funcao = input('Informe a funcao [cobrador|motorista]: ').lower()
        if funcao != 'cobrador' and funcao != 'motorista':
            print('Erro! Informe uma funcao valida.')
    return funcao

def verifica_id(funcao, ids_em_uso):
    id = ''
    if funcao == 'motorista':
        while len(id) != 2 or id in ids_em_uso or id_nao_int():
            id = input(
                "Informe o id: [4 numeros = cobrador| 2 numeros = motorista] ")
            if len(id) != 2 or id_nao_int():
                print('Erro! Informe o id no formato especificado.')
            if id in ids_em_uso:
                print('Erro! O id digitado ja esta em uso.')
    else:
        while len(id) != 4 or id in ids_em_uso or id_nao_int():
            id = input(
                "Informe o id: [4 numeros = cobrador| 2 numeros = motorista] ")
            if len(id) != 4 or id_nao_int():
                print('Erro! Informe o id no formato especificado.')
            if id in ids_em_uso:
                print('Erro! O id digitado ja esta em uso.')
    return id

def verifica_id_em_uso(ids_em_uso, funcionarios_em_atividade):
    id = ''
    while id not in ids_em_uso or id in funcionarios_em_atividade:
        id = input("Informe o id: ")
        if id not in ids_em_uso: 
            print('Erro! O id informado não existe.')
        if id in funcionarios_em_atividade:
            print('Erro! o funcionario esta atuando no momento.')
    return id

def verifica_salario():
    salario = 0
    while salario < 2500 or salario > 15000:
        salario = float(input('Informe o salario [2500 a 15000]: '))
        if salario < 2500 or salario > 15000:
            print('Erro! O salario esta fora do intervalo aceito.')
    return salario

def consultar_destinos(destinos):
    for destino in destinos:
        print(destino)

def adicionar_destino(destinos):
    destino = input('Informe um novo destino: ').lower()
    while destino in destinos:
        print('Erro! O destino informado ja esta cadastrado.')
        destino = input('Informe um novo destino: ').lower()
    return destino

def remover_destino(destinos):
    destino = ''
    while destino not in destinos:
        destino = input('Informe o destino a ser deletado: ').lower()
        if destino not in destinos:
            print('Erro! O destino informado nao existe.')
    return destino

def verifica_numeracao(numeracoes_em_uso):
    numero = ''
    while len(numero) != 4 or numero in numeracoes_em_uso:
        numero = input('Informe a numeracao do onibus [quatro numeros]: ')
        if len(numero) != 4:
            print('Erro! a numeracao deve conter quatro digitos.')
        if numero in numeracoes_em_uso:
            print('Erro! O numero digitado ja esta em uso.')
    return numero

def verifica_numeracao_em_uso(numeracoes_em_uso, onibus_em_atividade):
    numero = ''
    while numero not in numeracoes_em_uso or numero in onibus_em_atividade:
        numero = input('Informe o numero: ')
        if numero not in numeracoes_em_uso:
            print('Erro! Nao existe onibus com essa numeracao.')
        if numero in onibus_em_atividade:
            print('Erro! O onibus esta atuando no momento.')
    return numero

def verifica_destino(destinos, onibus_em_atividade,n):
    destino = ''
    if n in onibus_em_atividade:
        while destino != 'retornou':
            destino = input('Informe o destino ou informe retornou caso tenha retornado: ').lower()
            if destino != 'retornou':
                print('Erro! O onibus ja esta em viagem. Assim, so eh possivel retornar.')
    else:
        while destino not in destinos:
            destino = input('Informe o destino ou informe retornou caso tenha retornado: ').lower()
            if destino not in destinos:
                print('Erro! Informe um destino existente.')
            if destino == 'retornou':
                print('Observacao: O onibus ja nao estava em viagem')
    return destino

def verifica_funcionarios_atuando(funcionarios_em_atividade):
    id1 = ''
    id2 = ''
    while len(id1) != 4 and len(id1) != 2 or len(id2) != 4 and len(id2) != 2 or len(id1) == len(id2) or id1 in funcionarios_em_atividade or id2 in funcionarios_em_atividade:
        id1, id2 = input('Informe os IDs dos funcionarios separados por espaço [obs: eh necessario haver um motorista e um cobrador]: ').split()
        if len(id1) != 4 and len(id1) != 2 or len(id2) != 4 and len(id2) != 2 or len(id1) == len(id2):
            print('Erro! Escreva no formato especificado.')
        if id1 in funcionarios_em_atividade or id2 in funcionarios_em_atividade:
            print('Erro! Um dos ids informados ja esta em viagem.')
    return id1, id2

def id_nao_int(id):
    for valor in id:
        if valor != '0' and valor != '1' and valor != '2' and valor != '3' and valor != '4' and valor != '5' and valor != '6' and valor != '7' and valor != '8' and valor != '9':
            return True
        else:
            return False

def informacoes_final_expediente(lista_onibus, lista_funcionarios):
   
    quantidade_viagens_por_funcionario(lista_funcionarios)
    ainda_nao_retornou(lista_onibus)

def quantidade_viagens_por_funcionario(lista_funcionarios):
    for funcionario in lista_funcionarios:
        if funcionario.get_funcao() == 'cobrador':
            print(f'Funcionario: {funcionario.get_id_cobrador()}. Viagens realizadas: {funcionario.get_cont_viagens()}')
        else:
            print(f'Funcionario: {funcionario.get_id_motorista()}. Viagens realizadas: {funcionario.get_cont_viagens()}')

def ainda_nao_retornou(lista_onibus):
    cont = 0
    for onibus in lista_onibus:
        if onibus.get_status():
            print(f'Onibus: {onibus.get_numeracao()}')
            print(f'Funcionarios: {onibus.get_funcionarios_atuando()}')
            print(f'Destino: {onibus.get_destino()}')
            cont += 1
    if cont > 1:
        print('A policia ja foi acionada.')
    else:
        print('Todos retornaram.')

