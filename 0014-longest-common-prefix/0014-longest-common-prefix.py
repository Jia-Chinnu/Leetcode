class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Handle empty input
        if not strs:
            return ""
        
        # 1. Sort the strings alphabetically
        strs.sort()
        
        # 2. Grab the first and last strings
        first = strs[0]
        last = strs[-1]
        res = ""
        
        # 3. Compare them character by character
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return res
            res += first[i]
            
        return res