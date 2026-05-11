class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        hashmap={}
        for i in range(n):
            diff=target-nums[i]
            if diff in hashmap:
                return [hashmap[diff],i]
            hashmap[nums[i]]=i



        