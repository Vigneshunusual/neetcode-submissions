class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n=len(nums)
        maxcount=0
        curcount=0
        for i in range(n):
            if nums[i]==1:
                curcount+=1
                maxcount=max(maxcount,curcount)
            else:
                curcount=0
        return maxcount

        