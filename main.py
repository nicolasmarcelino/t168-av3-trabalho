from ops import *

# Ex. 3 (pág. 499)
# matriz = [[0,1,0,0,1,0,0,1,0,0],[0,0,0,0,1,0,0,0,0,0],[0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,1,1,0,0,0],[0,0,0,0,0,0,0,1,0,0],[0,1,1,1,1,0,0,1,0,1],[0,0,0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0],[0,0,0,0,0,1,0,0,0,0]]

# Ex. 5 (pág. 501)
matriz = [[0, 0, 1, 0], [1, 0, 0, 0], [1, 1, 0, 0], [0, 1, 0, 0]]

# Ex. 7 (pág. 501)
# matriz = [[0, 1, 1, 1, 0], [1, 0, 0, 0, 1], [0, 0, 0, 0, 1], [0, 1, 0, 0, 0], [0, 1, 1, 0, 0]]

matriz_t = transposta(matriz) # Matriz de adjacência transposta

for _ in range(0, 1):
    h = soma(matriz) # Vetor centro inicial
    a = soma(matriz_t) # Vetor autoridade inicial
    for _ in range(0,100):
        h = dividir_por_escalar(multiplicar_por_vetor(matriz, a), norma(multiplicar_por_vetor(matriz, a)))
        a = dividir_por_escalar(multiplicar_por_vetor(matriz_t, h), norma(multiplicar_por_vetor(matriz_t, h)))

# print("Vetor centro atualizado:", h)
# print("Vetor autoridade atualizado", a)

for index, value in enumerate(a):
    print(f"Site {index+1}: {value}")