class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max=float('-inf')
        cursum=0
        n=len(nums)
        for i in range(n):
            cursum+=nums[i]
            if cursum>max:
                max=cursum
            if cursum<0:
                cursum=0
        return max
