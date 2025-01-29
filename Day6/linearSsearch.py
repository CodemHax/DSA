def searchInSorted(arr, k):
    for i in range(len(arr)):
        if arr[i] == k:
            return True
        else:
            return False




arr = [1,3,4,5,6,7,8,90]
n = 10
print(searchInSorted(arr, n))