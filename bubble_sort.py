def bubble_sort(l: list) -> list:
    n = len(l)
    for i in range(n):
        for j in range(n-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    
    return l

print(bubble_sort([2,5,6,1,8,9,0]))