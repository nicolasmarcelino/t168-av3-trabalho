import math

def vector_norm(vector):
    sum_of_squares = 0
    for component in vector:
        sum_of_squares += component ** 2
    norm = math.sqrt(sum_of_squares)
    return norm

def mul(A, B):
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

def sum_rows(matrix):
    row_sums = []
    for row in matrix:
        row_sum = 0
        for value in row:
            row_sum += value
        row_sums.append(row_sum)
    return row_sums

def sum_columns(matrix):
    if not matrix or not matrix[0]:
        return []

    num_columns = len(matrix[0])
    column_sums = [0] * num_columns

    for row in matrix:
        for i in range(num_columns):
            column_sums[i] += row[i]
    
    return column_sums