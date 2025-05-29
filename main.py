from ops import *

matrix = [
    [0, 0, 1, 1],
    [1, 0, 0, 0],
    [1, 0, 0, 1],
    [1, 1, 1, 0]
]

h = sum_rows(matrix)
a = sum_columns(matrix)

print()

# print("Vetor centro inicial:", h)
# print("Vetor autoridade inicial:", a)
