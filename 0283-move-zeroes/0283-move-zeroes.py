class Solution:
    def moveZeroes(self, arr: list[int]) -> None:
       left=0
       right=0
       while(right<len(arr)):
            if arr[right]!=0:
                arr[left],arr[right]=arr[right],arr[left]
                left+=1
            right+=1
       return arr