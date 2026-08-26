class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        low=0
        high=0
        freq={}
        max_freq=-1
        max_len=-1
        while high<len(nums):
            freq[nums[high]]=freq.get(nums[high],0)+1
            # 2. Shrink when number of 0s exceeds k
            while freq.get(0, 0) > k:
                freq[nums[low]] -= 1
                if freq[nums[low]] == 0:
                    del freq[nums[low]]
                low += 1
            max_len = max(max_len, high - low + 1)
            high += 1
        return max_len