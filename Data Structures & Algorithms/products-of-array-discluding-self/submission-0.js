class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        let n=nums.length
        let left=1
        let result=new Array(n).fill(1)
        for(let i=0;i<n;i++){
            result[i]=left
            left=left*nums[i]
        }
        let right=1
        for(let i=n-1;i>=0;i--){
            result[i]=result[i]*right
            right=right*nums[i]
        }
        return result
    }
}
