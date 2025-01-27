def SecondLargestNumbersort(arr):
    arr.sort()
    seclargestnumber = len(arr) - 2
    print(arr[seclargestnumber])

# def SecondLargestNumber(arr):
#     largestnumber = 0
#     secondlargestnumber = 0
#     for i in arr:
#         if i > largestnumber:
#             # secondlargestnumber = largestnumber
#             largestnumber = i
#         if i > 0:
#             if i != largestnumber:
#                 secondlargestnumber = i
#
#     print(secondlargestnumber)

#
# def getSecondLargest(arr,n):
#     if n < 2:
#         return -1
#     large = second_largest = 0
#
#     for i in arr:
#         if i > large:
#             second_largest = large
#             large = i
#         elif i > second_largest and i != large:
#             second_largest = i
#     return second_largest

def secondLargest(arr, n):
    if n < 2:
        return -1
    large = float('-inf')
    second_large = float('-inf')
    for i in range(n):
        if (arr[i] > large):
            second_large = large
            large = arr[i]
        elif (arr[i] > second_large and arr[i] != large):
            second_large = arr[i]
    return second_large



# def secondLargest(arr, n):
#     if (n < 2):
#         return -1
#     large = float('-inf')
#     second_large = float('-inf')
#     for i in range(n):
#         if (arr[i] > large):
#             second_large = large
#             large = arr[i]
#         elif (arr[i] > second_large and arr[i] != large):
#             second_large = arr[i]
#     return second_large



if __name__ == "__main__":
    arr = [10, 10, 10,10]
    n = len(arr)
    print(secondLargest(arr, n))