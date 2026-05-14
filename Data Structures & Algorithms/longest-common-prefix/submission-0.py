class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=""
        for i in range(len(strs[0])):
            ch = strs[0][i]
            for s in strs:
                if i>=len(s) or ch != s[i]:
                    return prefix
            prefix += ch
        return prefix