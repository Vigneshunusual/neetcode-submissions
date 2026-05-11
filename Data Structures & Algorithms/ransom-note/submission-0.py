class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count={}
        m=magazine
        r=ransomNote
        for ch in m:  
            if ch in count:
                count[ch]+=1
            else:
                count[ch]=1
        for ch in r:
            if ch not in count:
                return False
            count[ch]-=1
            if count[ch]<0:
                return False
        return True
        