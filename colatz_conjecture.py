num = 256
print(num)
iterations = 1
while num != 1:
    if num % 2 == 0:
        num //= 2
    
    else:
        num = 3 * num + 1

    iterations += 1
    print(num)

print(f"{iterations=}")