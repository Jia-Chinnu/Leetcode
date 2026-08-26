class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        low=0
        high=0
        freq={}
        maxi=-1
        s=0
        while(high<len(fruits)):
            freq[fruits[high]]=freq.get(fruits[high],0)+1
            while len(freq)>2:
                freq[fruits[low]]-=1
                if freq[fruits[low]]==0:
                    del freq[fruits[low]]
                low+=1

            maxi=max(maxi,high-low+1)
            high+=1
        return maxi

        