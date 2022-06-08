#https://leetcode.com/problems/container-with-most-water/
#two pointer method
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        lb,ub = 0,len(height)-1
        while lb < ub:
            area = min(height[lb],height[ub])*(ub-lb)
            max_area = max(area,max_area)
            if height[lb] > height[ub]:
                ub -= 1
            else: lb += 1
        return max_area   