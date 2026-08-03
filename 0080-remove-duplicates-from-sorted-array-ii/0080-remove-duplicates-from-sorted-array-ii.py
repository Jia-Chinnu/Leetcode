class Solution:
    def removeDuplicates(self, arr: List[int]) -> int:
      
      j=0
      for i in range(2,len(arr)):
        if arr[i]!=arr[j]:
            j+=1
            arr[j+1]=arr[i]
      return j+2
