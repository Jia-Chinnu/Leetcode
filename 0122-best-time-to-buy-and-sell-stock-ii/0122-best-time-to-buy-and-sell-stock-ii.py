class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest=prices[0]
        sum=0
        for i in range(0,len(prices)):
            if (prices[i]<lowest):
                 lowest=prices[i]
            current= prices[i]-lowest
            if current>0:
                 sum=sum+current
                 lowest=prices[i]
        return sum