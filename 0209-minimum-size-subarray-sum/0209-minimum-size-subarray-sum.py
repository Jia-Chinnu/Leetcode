class Solution:
    def minSubArrayLen(self, target: int, arr: List[int]) -> int:
        low=0
        high=0
        n=len(arr)
        sum=0
        res = float('inf')
        while(high<n):
            sum+=arr[high]
            while(sum>=target):
                leng=high-low+1
                res=min(res,leng)
                sum-=arr[low]
                low+=1
            high+=1
        if res == float('inf'):
            return 0
        return res