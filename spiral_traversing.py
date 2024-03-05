import numpy as np

def spiral(a):
    k, l, m, n = 0, 0, a, a

    matrix = np.arange(1, a ** 2 + 1).reshape(a,a)
    print(matrix)

    while k < m and l < n:
        for i in range(l, n):
            print(matrix[k][i], end=" ")
        
        k += 1

        for i in range(k, m):
            print(matrix[i][n-1], end=" ")

        n -= 1

        if k < m:
            for i in range(n-1, l-1, -1):
                print(matrix[m-1][i], end=" ")
            m -= 1

        if l < n:
            for i in range(m-1, k-1, -1):
                print(matrix[i][l], end=" ")
            
            l += 1

spiral(5)