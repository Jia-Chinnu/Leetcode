class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        res=[]
        ans=[]
        for ch in s:
            if ch!='#':
                res.append(ch)
            elif res:  # Check that res is NOT empty before popping
                res.pop()
        for ch in t:
            if ch!='#':
                ans.append(ch)
            elif ans:
                ans.pop()
        if res==ans:
            return True
        else:
            return False

                
                    
            
            
        