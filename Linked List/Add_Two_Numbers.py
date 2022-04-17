# Link https://leetcode.com/problems/add-two-numbers/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1,num2 = 0,0
        count1,count2 = 1,1
        p = ListNode()
        while l1 is not None or l2 is not None:
            if l1:
                num1 = l1.val*count1 + num1
                count1*=10
                l1 = l1.next
            if l2:
                num2 = l2.val*count2 + num2
                count2*=10
                l2 = l2.next
        num = num1 + num2
        if num:
            headval = ListNode(num%10,None)
            num = num // 10
            p = headval
            while num > 0:
                d = ListNode(num%10,None)
                headval.next = d
                headval = headval.next
                num = num // 10
        return p