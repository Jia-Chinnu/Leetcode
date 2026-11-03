class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        ans=[]
     
        maxi=max(candies)
        for i in range(0,len(candies)):
            if (candies[i]+extraCandies)>=maxi:
              
                 ans.append(True)
            else:
                 ans.append(False)
        return ans
        