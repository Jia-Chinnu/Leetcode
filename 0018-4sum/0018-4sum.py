class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res=set()
        for i in range(len(nums)-3):
            for mid in range(i+1,len(nums)-2):
                low=mid+1
            
                high=len(nums)-1
                
                
                while(low<high):
                    sum=nums[i]+nums[low]+nums[high]+nums[mid]
                    if sum==target:
                        res.add((nums[i],nums[low],nums[mid],nums[high]))
                        low+=1
                
                        high-=1
                    elif sum<target:
                        low+=1
                        
                    else:
                        high-=1
        ans=[]
        for i in res:
                ans.append(list(i))
        return ans

                


        