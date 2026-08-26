class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        low=0
        high=0
        max_freq=-1
        max_len=-1
        freq={}
        while high<len(s):
            freq[s[high]]=freq.get(s[high],0)+1
            max_freq=max(max_freq,freq[s[high]])
            while (high-low+1)-max_freq>k:
                freq[s[low]]-=1
                if freq[s[low]]==0:
                    del freq[s[low]]
                low+=1
                
            max_len=max(max_len,high-low+1)
            high+=1
        return max_len
            
                

        