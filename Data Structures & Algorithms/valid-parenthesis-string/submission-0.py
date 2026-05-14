class Solution:
    def checkValidString(self, s: str) -> bool:
        minp = maxp = 0
        
        for c in s:
            if c == '(':
                maxp += 1
                minp += 1
            elif c == ')':
                maxp -= 1
                minp -= 1
            else:
                maxp += 1
                minp -= 1
            
            if maxp < 0:
                return False
            minp = max(0, minp)
        
        return minp == 0