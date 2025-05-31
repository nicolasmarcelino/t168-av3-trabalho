import math

def multiplicar_por_vetor(matriz, vetor):
    if len(matriz[0]) != len(vetor):
        raise ValueError("A quantidade de colunas da matriz deve ser igual ao tamanho do vetor")

    resultado = []
    for linha in matriz:
        produto_escalar = sum(m * v for m, v in zip(linha, vetor))
        resultado.append(produto_escalar)
    return resultado

def multiplicar_por_escalar(vetor, escalar):
    return [componente * escalar for componente in vetor]

def dividir_por_escalar(vetor, escalar):
    if escalar == 0:
        raise ValueError("Não é possível dividir por zero.")
    return [round(componente / escalar, 5) for componente in vetor]

def transposta(matriz):
    if not matriz:
        return []

    return [[linha[i] for linha in matriz] for i in range(len(matriz[0]))]

def norma(vetor):
    soma_dos_quadrados = 0
    for componente in vetor:
        soma_dos_quadrados += componente ** 2
    norma = math.sqrt(soma_dos_quadrados)
    return norma


def mult(A, B):
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            sum = 0
            for k in range(len(B)):
                sum += A[i][k] * B[k][j]
            row.append(sum)
        result.append(row)
    return result

def soma(matrix):
    row_sums = []
    for row in matrix:
        row_sum = 0
        for value in row:
            row_sum += value
        row_sums.append(row_sum)
    return row_sums

def vetor_centro(matrix):
    row_sums = []
    for row in matrix:
        row_sum = 0
        for value in row:
            row_sum += value
        row_sums.append(row_sum)
    return row_sums

def vetor_autoridade(matrix):
    if not matrix or not matrix[0]:
        return []

    num_columns = len(matrix[0])
    column_sums = [0] * num_columns

    for row in matrix:
        for i in range(num_columns):
            column_sums[i] += row[i]
    
    return column_sums