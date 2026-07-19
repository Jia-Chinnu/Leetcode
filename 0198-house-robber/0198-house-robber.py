class Solution:
    def rob(self, nums: list) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        prev2 = 0
        prev1 = 0

        for i in range(n):
            s = max(prev1, prev2 + nums[i])
            prev2 = prev1
            prev1 = s

        return s
