class Solution:
    def longestPalindrome(self, s: str) -> int:

        freq = {}

        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

        length = 0
        odd = False

        for ch in freq:
            if freq[ch] % 2 == 0:
                length += freq[ch]
            else:
                length += freq[ch] - 1
                odd = True

        if odd:
            length += 1

        return length