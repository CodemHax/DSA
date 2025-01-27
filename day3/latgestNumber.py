
def LargestNumber(arr):
    largestnumber = 0
    for i in arr:
        if i > largestnumber:
            largestnumber = i
    print(largestnumber)

def LargestNumbersort(arr):
    arr.sort()
    largestnumber = len(arr)
    print(arr[largestnumber])



if __name__ == "__main__":
   arr = [13,5,66,4,6,3,7,33,643]
   LargestNumber(arr)