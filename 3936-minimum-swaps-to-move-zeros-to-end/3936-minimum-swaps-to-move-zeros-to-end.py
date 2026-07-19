class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        z = nums.count(0)

        swaps = 0
        for i in range(len(nums) - z, len(nums)):
            if nums[i] != 0:
                swaps += 1

        return swaps