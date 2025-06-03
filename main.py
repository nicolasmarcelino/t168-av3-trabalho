from ops import *

# Ex. 3 (pág. 499)
# matriz = [[0,1,0,0,1,0,0,1,0,0],[0,0,0,0,1,0,0,0,0,0],[0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,1,1,0,0,0],[0,0,0,0,0,0,0,1,0,0],[0,1,1,1,1,0,0,1,0,1],[0,0,0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0],[0,0,0,0,0,1,0,0,0,0]]

# Ex. 5 (pág. 501)
# matriz = [[0, 0, 1, 0], [1, 0, 0, 0], [1, 1, 0, 0], [0, 1, 0, 0]]

# Ex. 6 (pág. 501)
# matriz = [[0,1,1,0], [0,0,1,0], [1,0,0,1], [1,0,0,0]]

# Ex. 7 (pág. 501)
# matriz = [[0, 1, 1, 1, 0], [1, 0, 0, 0, 1], [0, 0, 0, 0, 1], [0, 1, 0, 0, 0], [0, 1, 1, 0, 0]]

# Ex. 8 (pág. 501)
matriz = [[0, 1, 1, 0, 1, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 1, 1, 0, 0, 1, 1, 0, 0, 1], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 1, 1, 0, 0, 1, 0, 1, 0, 1], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]]

transposta = transpor(matriz)

for _ in range(0, 1):
    h = somar_entradas(matriz) # Vetor centro inicial
    a = somar_entradas(transposta) # Vetor autoridade inicial
    for _ in range(0,100):
        h = dividir(multiplicar(matriz, a), norma(multiplicar(matriz, a)))
        a = dividir(multiplicar(transposta, h), norma(multiplicar(transposta, h)))
        
for index, value in enumerate(arredonda(a)):
    print(f"Site {index+1}: {value}")