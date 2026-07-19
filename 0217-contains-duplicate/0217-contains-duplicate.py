class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq={}
        for ch in nums:
            if ch in freq:
                freq[ch]+=1
            else:
                freq[ch]=1
            if freq[ch]!=1:
                return True
            
        return False
        