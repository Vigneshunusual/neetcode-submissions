class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[1]*n
        l=0
        r=n-1
        k=n-1
        while(l<=r):
            leftsq=nums[l]*nums[l]
            rightsq=nums[r]*nums[r]

            if leftsq>rightsq:
                res[k]=leftsq
                l+=1
            else:
                res[k]=rightsq
                r-=1
            k-=1
        return res
            
           
           
        