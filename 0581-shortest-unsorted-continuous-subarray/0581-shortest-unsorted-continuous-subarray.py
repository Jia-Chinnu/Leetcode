class Solution:
    def findUnsortedSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 1:
            return 0
            
        low = 0
        high = n - 1
        
        # 1. Shrink low from left
        while low < n - 1 and arr[low] <= arr[low + 1]:
            low += 1
            
        # Already fully sorted!
        if low == n - 1:
            return 0
            
        # 2. Shrink high from right
        while high > 0 and arr[high] >= arr[high - 1]:
            high -= 1
            
        # 3. Find min & max inside the middle window
        sub_min = min(arr[low:high + 1])
        sub_max = max(arr[low:high + 1])
        
        # 4. Expand outward if middle elements demand a wider range
        while low > 0 and arr[low - 1] > sub_min:
            low -= 1
            
        while high < n - 1 and arr[high + 1] < sub_max:
            high += 1
            
        # 5. Fixed length formula: high - low + 1
        s = high - low + 1
        return s