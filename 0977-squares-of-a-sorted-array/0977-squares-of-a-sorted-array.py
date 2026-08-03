class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans=[]
        res=[]
        for i in nums:
            if i<0:
                res.append(i)
            else:
                ans.append(i)
        res.reverse()
        for i in range(len(ans)):
            ans[i]=ans[i]*ans[i]
        for i in range(len(res)):
            res[i]=res[i]*res[i]
        i=0
        j=0
        f=[]
        while i<len(ans) and j<len(res):
            if ans[i]<=res[j]:
                f.append(ans[i])
                i+=1
            else:
                f.append(res[j])
                j+=1
        while(i<len(ans)):
                f.append(ans[i])
                i+=1
        while(j<len(res)):
                f.append(res[j])
                j+=1
        for k in range(len(res)+len(ans)):
            nums[k]=f[k]
        return nums


