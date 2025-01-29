def pushToEndZero(nums):
    j = 0
    for i in range(len(nums)):
        if nums[i] != 0 :
           nums[j], nums[i] = nums[i], nums[j]
           j += 1
    return nums


def searchInSorted(self, arr, k):
    for i in range(len(arr)):
        if arr[i] == k:
            return True
