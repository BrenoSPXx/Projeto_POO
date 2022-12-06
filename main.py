from funcoes import intervalo_tempo_int
from funcoes import verificacao_intervalo_tempo
from funcoes import add_lista
from funcoes import del_lista
from funcoes import alterar_lista
from funcoes import print_lista
from funcoes import rotina_print
from funcoes import predefinicoes

from funcionario import Funcionario

def main():
    while True:
        op_1 = ''
        op_2 = 's'
        cont_expediente = 1
        cont_tempo = 8
        cont_intervalo_tempo = ''
       
        #predefinicoes
        func1, func2, func3, func4, func5, func6, oni1, oni2, oni3, oni4, oni5 = predefinicoes() 
        funcionarios = [func1, func2, func3, func4, func5, func6]
        veiculos = [oni1, oni2, oni3, oni4, oni5]
        destinos = ['Condado', 'Gondor', 'Mordor', 'Moçambique', 'Trindade']
        
        lista_nome = ['funcionarios', 'veículos', 'destinos']
        
        print('=-' * 25)
        print('SISTEMA DE VERIFICAÇÃO DO TERMINAL DE ÔNIBUS')
        print('=-' * 25)
        print('\nInício do expediente: 8:00h | Final do expediente: 20:00h ')
        while verificacao_intervalo_tempo(cont_intervalo_tempo):
            cont_intervalo_tempo = input('\nInforme de quanto em quanto tempo haverá uma nova verificação[Exemplos: 0:30h, 1:00h, etc], [obs: o intervalo de tempo deve ser menor ou igual a 6h(metade do expediente) e maior que 0]: ').lower()
            if verificacao_intervalo_tempo(cont_intervalo_tempo):
                print('\nErro! Digite no formato especificado.')
        
        print('\nDIA {}\n'.format(cont_expediente))
        rotina_print(funcionarios, veiculos, destinos, lista_nome)
        funcionarios = alterar_lista(funcionarios, lista_nome[0])
        veiculos = alterar_lista(veiculos, lista_nome[1])
        while op_2 == 's':
            cont_tempo += intervalo_tempo_int(cont_intervalo_tempo)
            if cont_tempo == 20:
                op_2 = ''
                cont_expediente += 1
                cont_tempo = 8    
                while op_2 != 's' and op_2 != 'n':
                    op_2 = input('\nDeseja continuar e seguir para o próximo dia[s/n]? ').lower()
                    if op_2 != 's' and op_2 != 'n':
                        print('Erro! Digite "s", caso deseje continuar no programa ou "n", caso não.')
                if op_2 == 'n':
                    break
                else:
                    print('\nDIA {}\n'.format(cont_expediente))
                    rotina_print(funcionarios, veiculos, destinos, lista_nome)
                    funcionarios = alterar_lista(funcionarios, lista_nome[0])
                    veiculos = alterar_lista(veiculos, lista_nome[1])
                
        while op_1 != 's' and op_1 != 'n':
            op_1 = input('\nDeseja continuar no programa[s/n]? (Os valores serão reinicializados) ').lower()
            if op_1 != 's' and op_1 != 'n':
                print('Erro! Digite "s", caso deseje continuar no programa ou "n", caso não.')
        if op_1 == 'n':
            print('Fim do programa.')
            break
main()