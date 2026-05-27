class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first=strs[0]
        for i in range(len(first)):
            ch=first[i]
            for word in strs[1:]:
                if word[i]!=ch or i>=len(word):
                    return first[:i]
        return first
        