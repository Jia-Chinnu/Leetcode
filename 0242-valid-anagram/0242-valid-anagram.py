class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 1. If lengths are different, they can't be anagrams
        if len(s) != len(t):
            return False
        
        t_list = list(t)
        for ch in s:
            if ch in t_list:
                t_list.remove(ch) # Remove so it's not counted twice
            else:
                return False
        
        # 2. If the loop finishes, all characters matched!
        return True