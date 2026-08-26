class Solution:
    def minWindow(self, s: str, t: str) -> str:
        low = 0
        high = 0
        freq = {}
        target = {}
        min_len = float("inf")
        res = [-1, -1]

        for c in t:
            target[c] = target.get(c, 0) + 1

        have = 0
        need = len(target)

        while high < len(s):
            # 1. Add current element to frequency map
            freq[s[high]] = freq.get(s[high], 0) + 1

            if s[high] in target and freq[s[high]] == target[s[high]]:
                have += 1

            # 2. Shrink when all required characters are satisfied
            while have == need:
                if (high - low + 1) < min_len:
                    min_len = high - low + 1
                    res = [low, high]

                freq[s[low]] -= 1
                if s[low] in target and freq[s[low]] < target[s[low]]:
                    have -= 1
                if freq[s[low]] == 0:
                    del freq[s[low]]
                low += 1

            high += 1

        return s[res[0]:res[1] + 1] if min_len != float("inf") else ""