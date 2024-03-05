n = 15
magic_square = [[0 for _ in range(n)] for _ in range(n)]

magic_num = int(n*(n**2 + 1)/2)

for i in range(1, n**2 + 1):
    if i == 1:
        p, q = n//2, n-1
        magic_square[p][q] = 1

    else:
        p -= 1
        q += 1
        if p == -1 and q == n:
            p = 0 
            q = n -2
        elif p == -1:
            p = n-1
        elif q == n:
            q = 0
        
        if magic_square[p][q] != 0:
            q -= 2
            p += 1

        magic_square[p][q] = i

for row in magic_square:
    for value in row:
        print(value, end=' ')
    print()
print("The sum of each row/colum/diagonal:", magic_num)