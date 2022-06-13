#https://leetcode.com/problems/product-of-array-except-self/
#Right product & Left product
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, suffix = 1,1
        res = [1]*len(nums)
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        for i in range(len(nums)-1,-1,-1):
            res[i] *= suffix
            suffix *= nums[i]
        return res