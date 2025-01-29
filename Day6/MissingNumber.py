from typing import List


def missingNumber(array : List[int]):
     total_sum = sum(range(0, len(array) + 1))
     actual_sum = sum(array)
     return total_sum - actual_sum

# def missingNumber(array : List[int]):
    # for i in range(len(array) + 1):
    #     if i not in array:
    #         return i




if __name__ == "__main__":
    arr = [0,1]
    n = 2
    print(missingNumber(arr))