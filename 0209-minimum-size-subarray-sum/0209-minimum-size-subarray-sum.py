class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        low=0
        high=0
        s=0
        res=float('inf')
        for high in range(len(nums)):
            s+=nums[high]
            while(s>=target):
                slen=high-low+1
                res=min(res,slen)
                s-=nums[low]
                low+=1
        return res if res!= float('inf') else 0

