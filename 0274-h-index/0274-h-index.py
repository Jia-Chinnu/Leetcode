class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n=len(citations)
        papercount=[0]*(n+1)
        for c in citations:
            papercount[min(n,c)]+=1
        h=n
        papers=papercount[n]
        while papers<h:
            h-=1
            papers+=papercount[h]
        return h
