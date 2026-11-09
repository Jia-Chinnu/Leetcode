class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        s=0
        for i in nums:
            s=s+i
        n=len(nums)
        total=n*(n+1)//2
        res=total-s
        return res