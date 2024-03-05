def binary_search_iter(array: list, element: int) -> None:
    first, last = 0, len(array) - 1
    iterations = 0

    while first <= last:
        mid = (first + last) // 2
        if array[mid] == element:
            print(f"The element is found at {mid}\nRequired {iterations} iterations.")
            return None
        
        elif array[mid] < element:
            first = mid + 1

        else:
            last = mid - 1
        iterations += 1

    print("Not found")

def binary_search_rec(array: list, element: int, low: int, high: int):
    if low == high:
        if array[high] == element:
            return high
        else: 
            return False
    
    mid = (low + high) // 2

    if array[mid] == element:
        return mid
    
    elif array[mid] < element:
        return binary_search_rec(array, element, mid+1, high)
    
    else:
        return binary_search_rec(array, element, low, mid-1)
    
a = list(range(0, 1000000, 3))
binary_search_iter(a, 83658)
print(binary_search_rec(a, -83658, 0, len(a) - 1))