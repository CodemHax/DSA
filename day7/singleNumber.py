from typing import List

from sqlalchemy.dialects.postgresql import array


# def singleNumber(arr: List[int]):
#     single = 0
#     if len(arr) <= 1 :
#         return arr[0]
#     for i in range(len(arr)):
#         if arr.count(arr[i]) == 1 :
#             single = arr[i]
#     return single

def singleNumber(nums):
    dic = dict()
    for i in nums:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

    for key , value in dic.items():
      if value == 1:
          return key


if __name__ == "__main__":
    arr = [-1,-1,-2]
    print(singleNumber(arr))