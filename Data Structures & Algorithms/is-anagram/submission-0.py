class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        resultS = "".join(sorted(s))
        resultT = "".join(sorted(t))
        
        if resultS == resultT:
            return True
        else:
            return False
        