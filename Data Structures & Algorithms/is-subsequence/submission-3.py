class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        slen = 0
        if len(s)==0:
            return True
        while i<len(s) and j<len(t):
            if s[i]==t[j]:
                slen = slen+1
                i = i+1
            j = j+1
            if slen==len(s):
                return True
        return False