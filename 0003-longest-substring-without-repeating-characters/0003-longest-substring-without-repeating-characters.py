class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        low=0
        high=0
        freq={}
        maxi=-1
       
        while high<len(s):
            freq[s[high]]=freq.get(s[high],0)+1
            k=high-low+1
            
            while len(freq)<k:
                freq[s[low]]-=1
                if freq[s[low]]==0:
                    del freq[s[low]]
                
                
                low+=1
                k=high-low+1
            maxi=max(maxi,k)
            high+=1
        return maxi if maxi>=1 else 0