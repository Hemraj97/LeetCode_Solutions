#https://leetcode.com/problems/kth-largest-element-in-an-array/
#Find an effiecient way to sort the array like quicksort
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums)-k]