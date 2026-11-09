class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        freq={}
        res=[]
        for ch in nums:
            if ch  in freq:
                freq[ch]+=1
            else:
                freq[ch]=1
        for ch,c in freq.items():
            if c>=2:
                res.append(ch)
        return res