class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest=float('inf')
        for i in range(len(nums)-2):
            if  i>0 and nums[i]==nums[i-1]:
                continue
            low=i+1
            high=len(nums)-1
            while(low<high):
                sum=nums[i]+nums[low]+nums[high]
                if abs(sum-target)<abs(closest-target):
                    closest=sum
                if sum==target:
                    return sum
                elif sum<target:
                    low+=1
                else:
                    high-=1
        return closest
                
                    

