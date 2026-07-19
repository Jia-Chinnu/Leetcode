class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Convert to a list ONCE so we can keep track of used letters
       freq={}
       for ch in magazine:
        if ch in freq:
            freq[ch]+=1
        else:
            freq[ch]=1
       for ch in ransomNote:
        if ch not in freq or freq[ch]==0 :
            return False
        freq[ch]-=1
       return True