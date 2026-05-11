class Solution:
    def firstUniqChar(self, s: str) -> int:
        n=len(s)
        count={}
        for ch in s:
            if ch in count:
                count[ch]+=1
            else:
                count[ch]=1
            
        for i in range(n):
            if count[s[i]]==1:
                return i
        return -1
        