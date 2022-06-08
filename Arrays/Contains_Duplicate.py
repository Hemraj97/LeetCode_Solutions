#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)