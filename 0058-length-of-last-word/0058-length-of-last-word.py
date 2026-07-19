class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word=s.split()
        if  not word:
            return 0
        latword=word[-1]
        return len(latword)
         