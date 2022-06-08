#https://leetcode.com/problems/maximum-subarray/
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res, cur = nums[0], 0
        for n in nums:
            cur += n
            if cur > res:
                res = cur
            if cur < 0:
                cur = 0
        return res