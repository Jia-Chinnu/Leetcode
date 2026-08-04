class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res=[]
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            low=i+1
            high=len(nums)-1
            sum=-1*nums[i]
           
            while(low<high):
                if nums[low]+nums[high]==sum:
                    res.append([nums[i], nums[low], nums[high]])
                    
                    low+=1
                    high-=1
                    while(low<len(nums) and nums[low]==nums[low-1] ):
                        low+=1
                    while(high>=0 and nums[high]== nums[high+1] ):
                        high-=1
                elif  nums[low]+nums[high]<sum:
                    low+=1
                elif  nums[low]+nums[high]>sum:
                    high-=1
                
        return res        
