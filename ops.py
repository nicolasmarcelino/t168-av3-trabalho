import math

def transpor(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    matriz_transposta = []
    for j in range(colunas):
        nova_linha = []
        for i in range(linhas):
            nova_linha.append(matriz[i][j])
        matriz_transposta.append(nova_linha)
    return matriz_transposta
    
def somar_entradas(matriz):
    vetor_somas = []
    for linha in matriz:
        soma = 0
        for elemento in linha:
            soma += elemento
        vetor_somas.append(soma)
    return vetor_somas

def multiplicar(matriz, vetor):
    resultado = []
    for linha in matriz:
        soma = 0
        for i in range(len(vetor)):
            soma += linha[i] * vetor[i]
        resultado.append(soma)
    return resultado

def norma(vetor):
    soma_quadrados = 0
    for elemento in vetor:
        soma_quadrados += elemento ** 2
    return math.sqrt(soma_quadrados)

def dividir(vetor, escalar):
    resultado = []
    for elemento in vetor:
        resultado.append(elemento / escalar)
    return resultado

def arredonda(vetor):
    resultado = []
    for elemento in vetor:
        resultado.append(round(elemento, 5))
    return resultado