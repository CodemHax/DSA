def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        mini = i
        for j in range(i + 1, n):
            if arr[j] < arr[mini]:
                mini = j
        arr[i] , arr[mini]  = arr[mini],arr[i]
    return arr




if __name__ == "__main__":
    arr = [4 ,1, 3, 9, 7]
    print(selectionSort(arr))






