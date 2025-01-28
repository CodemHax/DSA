
def rotate(nums ,k):
    # if len(nums) <= 1 or k == 0 :
    #     return nums
    # if k > len(nums):
    #     k = 1
    # else:
    #     k = k
    # n = len(nums) - k
    n = (len(nums) - k) % len(nums)
    print(n)
    toro = nums[n:]
    front = nums[:n]
    nums[:] = toro + front
    return nums



if __name__ == "__main__":
    numbs = [1,2,3,4,5,6,7,88]
    k = 11
    print(rotate(numbs, k))
