class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest=prices[0]
        c=0
        for i in range(1,len(prices)):
            if prices[i]<lowest:
                lowest=prices[i]

            elif prices[i]-lowest>c:
                c=prices[i]-lowest
        return c