class Solution:
    def sortedSquares(self, nums):
        neg = []
        pos = []

        for x in nums:
            if x < 0:
                neg.append(x * x)
            else:
                pos.append(x * x)

        neg.reverse()

        ans = []
        i = 0
        j = 0

        while i < len(neg) and j < len(pos):
            if neg[i] < pos[j]:
                ans.append(neg[i])
                i += 1
            else:
                ans.append(pos[j])
                j += 1

        while i < len(neg):
            ans.append(neg[i])
            i += 1

        while j < len(pos):
            ans.append(pos[j])
            j += 1

        return ans    