import random
def get_matrix (n,m,value):
    matrix=[]
    for i in range (n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
        print(matrix)
    return matrix
result1=get_matrix(2,2,10)
print(result1)
result2=get_matrix(3 ,5 ,42)
print(result2)
result3=get_matrix(4 ,2 ,13)
#print(result1)
#print(result2)
print(result3)

#print(get_matrix)
#n = int(input('Введите количество строк матрицы :  '))
#m = int(input('Введите количество столбцов матрицы :  '))
#value = input(f'Введите значение матрицы :  ')
#print('---------------------'*m)
#matrix = get_matrix(n, m, value)
#print('--'*m)
#if n <= 0:
#    print("Матрица пуста,задано неверное количество сторок:" ,n)
#elif m <=0:
#    print("Матрица пуста, задано неверное количество столбцов:  ",m)
#else:
#    print("Матрица :")
#     for i in matrix :
#         print(*i)
