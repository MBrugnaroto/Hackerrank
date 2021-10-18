
if __name__ == '__main__':

    matrix = [[112,42,83,119],
             [56,125,56,49],
             [15,78,101,43],
             [62,98,114,108]]

    n = len(matrix)
    t = int(n/2)

    column = [value[t] for value in matrix][::-1]

    for i in range(n):
        row = matrix[i].copy()
        row[t] = column[i]
        matrix[i] = row
    
    matrix[0] = matrix[0][::-1]
    somatorio = 0

    for i in range(t):
        row = matrix[i]
        aux = sum(row[0:t])
        somatorio += aux

    print(somatorio)