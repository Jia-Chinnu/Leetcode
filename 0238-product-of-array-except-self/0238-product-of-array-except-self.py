class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)

        answer = [1] * n
        prefix = 1
        suffix = 1

        for i in range(n):
            answer[i] *= prefix
            prefix *= nums[i]

            answer[n - 1 - i] *= suffix
            suffix *= nums[n - 1 - i]

        return answer