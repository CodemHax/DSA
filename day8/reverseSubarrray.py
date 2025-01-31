
def reverseArray(arr, m):
    back = arr[m+1:]
    back.reverse()
    front = arr[:m+1]
    arr[:] = front + back
    return arr

    pass
arr = [1, 2, 3, 4, 5, 6]
k = 3
print(reverseArray(arr, k))