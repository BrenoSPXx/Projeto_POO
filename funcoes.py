from funcionario import Funcionario
from onibus import Onibus
def intervalo_tempo_int(cont_intervalo_tempo):
    hora = int(cont_intervalo_tempo[0])
    hora_fracao_string = cont_intervalo_tempo[2] + cont_intervalo_tempo[3]
    hora_fracao = float(hora_fracao_string) / 60
    return hora + hora_fracao           
def verificacao_intervalo_tempo(cont_intervalo_tempo):
    if len(cont_intervalo_tempo) == 5 and cont_intervalo_tempo.count('h') == 1 and cont_intervalo_tempo[len(cont_intervalo_tempo) - 1] == 'h' and cont_intervalo_tempo.count(':') == 1 and cont_intervalo_tempo[len(cont_intervalo_tempo) - 4] == ':':
        cont_num = 0 
        cont_0 = 0
        for i in cont_intervalo_tempo:
            if i != ':' and i != 'h':
                if i == '0' or i == '1' or i == '2' or i == '3' or i == '4' or i == '5' or i == '6':
                    cont_num += 1
                    if i == '0':
                        cont_0 += 1
        if cont_num == 3 and cont_0 < 3:
            return False
        else:
            return True
    else:
        return True 
def add_lista(lista,n,lista_nome):
    for i in range(n):
        string_nome = ''
        string_funcao = ''
        while len(string_nome) > 10 or len(string_nome) < 3 or (string_funcao != 'cobrador' and string_funcao != 'motorista'):
            string_nome = input('Informe o(a) {}o(a) novo(a) integrante dos {}[10 > string > 3 ]: '.format(i + 1, lista_nome))
            string_funcao = input('Informe a funcao do novo(a) integrante dos {}:  '.format(lista_nome)).lower()
            if (len(string_nome) > 10 or len(string_nome) < 3) and len(string_funcao) != 9 and len(string_funcao) != 8:
                print('Erro! Escreva no formato especificado.')
        func = Funcionario(string_nome, string_funcao)
        lista.append(func)
    return lista
def del_lista(lista,n,lista_nome):
    for i in range(n):
        string = ''
        condicao = False
        objeto = object
        while condicao == False:
            cont = 0
            string = input('Informe o {}o a ser deletado de {}: '.format(i + 1, lista_nome))
            for j in lista:
                if j.get_nome() != string:
                    cont += 1
                else:
                    objeto = j
            if cont != len(lista):
                condicao = True
        lista.remove(objeto)
    return lista

    return lista
def alterar_lista(lista, lista_nome):
    op = ''
    op_del = ''
    op_add = ''
    quantidade_del = 0
    quantidade_add = 0
    while op != 's' and op != 'n':
        op = input('\nDeseja alterar a lista de {}[s/n]? '.format(lista_nome)).lower()
        if op != 's' and op != 'n':
            print('\nErro! Digite "s", caso deseje alterar ou "n", caso não: ')
    if op == 's':
        while op_del != 's' and op_del != 'n':
            op_del = input('\nDeseja deletar algum {} da lista[s/n]? '.format(lista_nome)).lower()
        if op_del != 's' and op_del != 'n':
            print('\nErro! Digite "s", caso deseje deletar ou "n", caso não: ')
       
        if op_del == 's':
            while quantidade_del < 1 or quantidade_del > 20:
                quantidade_del = int(input('\nInforme a quantidade de {} para deletar[{} >= quantidade >= 1]: '.format(lista_nome, len(lista))))
                if quantidade_del < 1 or quantidade_del > len(lista):
                    print('\nErro! Número informado está fora dos limites')
            lista = del_lista(lista,quantidade_del, lista_nome)
       
        while op_add != 's' and op_add != 'n':
            op_add = input('\nDeseja adicionar {}[s/n]? '.format(lista_nome)).lower()
            if op_add != 's' and op_add != 'n':
                print('\nErro! Digite "s", caso deseje adicionar ou "n", caso não: ')
       
        if op_add == 's':
            while quantidade_add < 1 or quantidade_add > 20:
                quantidade_add = int(input('\nInforme a quantidade de {} para adicionar[20 >= quantidade >= 1]: '.format(lista_nome)))
                if quantidade_add < 1 or quantidade_add > 20:
                    print('\nErro! Número informado está fora dos limites')
            lista = add_lista(lista,quantidade_add,lista_nome)
        return lista
        
    else:
        return lista
def print_lista(lista, lista_nome):
    print('Relação de {}:\n'.format(lista_nome))
    for i in lista:
        print(i)
    print()
def rotina_print(funcionarios, veiculos, destinos, lista_nome):
    print_lista(funcionarios, lista_nome[0])
    print_lista(veiculos, lista_nome[1])
    print_lista(destinos, lista_nome[2])
def predefinicoes():
    return Funcionario('Roberto', 'motorista'), Funcionario('Carla', 'motorista'), Funcionario('Carlos', 'motorista'), Funcionario('Miguel', 'cobrador'), Funcionario('Helena', 'cobrador'), Funcionario('Laura', 'cobrador'), Onibus('1234',''), Onibus('1324',''), Onibus('4231',''), Onibus('1432',''), Onibus('1423', '')