class Solution:
    def minSubArrayLen(self, target: int, arr: List[int]) -> int:
       low=0
       high=0
       s=0
       leni=0
       res=float('inf')
       n=len(arr)
       while(high<n):
        s=s+arr[high]
        while(s>=target):
            leni=high-low+1
            res=min(res,leni)
            s=s-arr[low]
            low+=1
            
        high+=1
       if res== float('inf'):
            return 0
       return res
