class Solution:
    def sortedSquares(self, nums):
        neg=[]
        pos=[]
        for i in range(len(nums)):
            if nums[i]<0:
                neg.append(nums[i])
                i+=1
            else:
                pos.append(nums[i])
        for i in range(len(neg)):
            neg[i]=neg[i]*neg[i]
        for j in range(len(pos)):
            pos[j]=pos[j]*pos[j]
        neg.reverse()
        i=0
        j=0
        ans=[]
        
        while(i<len(neg) and j<len(pos)):
            if neg[i]<pos[j]:
                ans.append(neg[i])
                i+=1
            else:
                ans.append(pos[j])
                j+=1
        while(i<len(neg)):
            ans.append(neg[i])
            i+=1
        while(j<len(pos)):
            ans.append(pos[j])
            j+=1
        return ans
              
            