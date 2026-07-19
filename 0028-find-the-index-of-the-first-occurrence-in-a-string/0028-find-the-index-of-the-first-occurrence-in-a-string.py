class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        
        # Loop through haystack, but stop when there isn't 
        # enough room left for the needle to fit
        for i in range(n - m + 1):
            # Check if the substring starting at i matches needle
            if haystack[i : i + m] == needle:
                return i
                
        return -1