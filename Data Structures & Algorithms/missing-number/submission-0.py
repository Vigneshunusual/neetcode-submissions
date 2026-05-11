class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        e_sum=n*(n+1)//2   
        a_sum=0            
        for i in nums:
            a_sum+=i
        return e_sum-a_sum
        