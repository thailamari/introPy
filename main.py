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




#estrutura de identificação / execução do script
if __name__ == '__main__':
    print_hi('Thaila')

    # chamar a função de cálculo da área do retângulo
    resultado = calcular_area_do_retangulo(3,4)
    print(f'A área do retângulo é de {resultado}m²')

    # chamar a função de cálculo da área do quadrado
    resultado = calcular_area_do_quadrado(5)
    print(f'A área do quadrado é de {resultado}m²')

    #chamar a função de cálculo a área do triângulo
    resultado = calcular_area_do_triangulo(6,7)
    print(f'A área do triângulo é de {resultado}m²')

    #executar uma contagem progressiva
    realizar_contagem_progressiva(11)

    #apoiar candidato
    apoiar_candidato('Bolsonaro',10)

    #contagem PLIM
    brinca_de_plim(100)