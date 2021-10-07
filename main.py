# 1 - Imports / bibliotecas

# 2 - Classe

# 3 - Métodos (faz algo sem retorno) e Funções (faz alguma coisa e retorna algum valor)

# def = definition = definição


def print_hi(name):
    print(f'Hi, {name}') # a partir do python 3
    print('Oi, ' + name) # antes do python 3

def calcular_area_do_retangulo(largura, comprimento):
    return largura * comprimento

def calcular_area_do_quadrado (lado):
    return lado ** 2

def calcular_area_do_triangulo (largura, comprimento):
    return largura * comprimento / 2

def realizar_contagem_progressiva(fim):
    for numero in range(fim): # repetir o bloco do zero até o fim
        print(numero)         # exibir o número

def apoiar_candidato(nome, vezes):
    for numero in range(vezes):
       # contador = numero + 1
       # print(f'{contador} - {nome}')

       if numero < 9:
           print(f'0{numero+ 1} - {nome}')
       elif numero < 99:
           print(f'0{numero + 1} - {nome}')
       else:
           print(numero + 1,'-',nome)

def brinca_de_plim(fim):
    for numero in range(fim):
        if numero % 4 == 0:
            print('PLIM!!')
        else:
            print('{:0>3}'.format(numero))
def sair(letra):
    print('Obrigado e Volte Sempre')


#Menu

#estrutura de identificação / execução do script
if __name__ == '__main__':


    resposta = 'c'

    while resposta.upper() != "Z":

        print('*************************************************')
        print('*               Menu de Opções                  *')
        print('*************************************************')
        print('*           1 - Olá Nome                        *')
        print('*           2 - Área do Retângulo               *')
        print('*           3 - Área do Quadrado                *')
        print('*           4 - Área do Triângulo               *')
        print('*           5 - Contagem Progressiva            *')
        print('*           6 - Apoiar Candidato                *')
        print('*           7 - Brincar de PLIM                 *')
        print('*********   Z - Sair                 ************')

        resposta = input("Escolha sua opção")
        print(f'A sua escolha foi: {resposta}')
        #sair('z')

        if resposta.upper() != 'Z':
            if resposta == '1':
                print_hi('Thaila')
            elif resposta == '2':
                resultado = calcular_area_do_retangulo(3,4)
                print(f'A área do Retângulo é de {resultado}m²')
            elif resposta == '3':
                resultado = calcular_area_do_quadrado(5)
                print(f'A área do Quadrado é de {resultado}m²')
            elif resposta == '4':
                resultado = calcular_area_do_triangulo(5,6)
                print(f'A área do Triângulo é de {resultado}m²')
            elif resposta == '5':
                realizar_contagem_progressiva(10)
            elif resposta == '6':
                apoiar_candidato('Mito', 10)
            elif resposta == '7':
                brinca_de_plim(50)
            else:
                print('Você digitou uma opção inválida. Escolha uma opção de 1 a 7')
        else:
             print('Você escolheu sair. Volte Sempre!!!')



