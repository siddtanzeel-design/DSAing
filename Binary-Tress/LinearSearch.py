def LinearSearch(arr, key):
    n = len(arr)

    for i in range(n):
        if arr[i] == key:
            return i+1

    return -1

arr = [1,5,7,9,10,15]
key = 9

print(LinearSearch(arr, key))
