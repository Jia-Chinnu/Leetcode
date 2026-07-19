class Solution:
    def majorityElement(self, nums: List[int]) -> int:
      freq={}
      maxi=0
      for ch in nums:
        if ch in freq:
            freq[ch]+=1
        else:
            freq[ch]=1
        if freq[ch]>maxi:
            maxi=freq[ch]
            ans=ch
      return ans
            
        