class Solution:
    def scoreOfString(self, s: str) -> int:
        i=0
        j=1
        ans=0
        for ch in range(len(s)-1):
            ans += abs(ord(s[i])-ord(s[j]))
            i += 1
            j += 1
        return ans
        