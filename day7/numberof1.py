def findMaxConsecutiveOnes(nums):
    count = 0
    max_count = 0
    for i in range(len(nums)):
         if nums[i] == 1:
             count+= 1
             print("count : ", count)
             print("max_count", max_count)
             max_count = max_count if count <= max_count else count
         else:
             count = 0
    return max_count




if __name__ == "__main__":
    arr = [1,1,0,1,1,1]
    print(findMaxConsecutiveOnes(arr))