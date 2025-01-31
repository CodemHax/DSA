#needredo
def longestSubarrayWithSumK(a, k):
    n = len(a)
    r = a.reverse()
    print(r)
    print(a)
    cur_sum = 0
    max_len = 0
    cur_sum_map = {}

    for i in range(n):
        cur_sum += a[i]

        if cur_sum == k:
            max_len = i + 1

        if (cur_sum - k) in cur_sum_map:
            max_len = max(max_len, i - cur_sum_map[cur_sum - k])

        if cur_sum not in cur_sum_map:
            cur_sum_map[cur_sum] = i

    return max_len


arr = [10, 5, 2, 7, 1, -10, 00]
k = 15
print(longestSubarrayWithSumK(arr, k))
