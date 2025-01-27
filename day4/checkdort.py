from time import perf_counter


class Solution(object):
  def check(self, nums):
    for i in range(len(nums) - 1):
        if nums[i] > nums[i+1]:
            print("list not sorted in ascending order")
            return False
    print("list sorted in ascending order")
    return True




if __name__ == "__main__":
    nums3 = [1, 10 , 1]
    print(Solution().check(nums3))



