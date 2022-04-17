# Link https://leetcode.com/problems/swap-nodes-in-pairs/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        root = head.next if head.next else head
        x = None
        while head and head.next:
            p = head
            head = head.next
            p.next = head.next if head.next else None
            head.next = p
            if x:
                x.next=head
                x = head.next
            else:
                x=head.next
            head = head.next.next if head.next.next else None 
        return root