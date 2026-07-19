class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # If the mappings are unique, the sets of zip and individual chars will match
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))