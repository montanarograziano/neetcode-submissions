# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        cur = head
        while cur:
            l += 1
            cur = cur.next
        
        k = l - n
        i = 0
        dummy = ListNode(0, head)
        cur = head
        prev = dummy
        while i < k:
            prev = cur
            cur = cur.next
            i += 1
        
        prev.next = cur.next
        return dummy.next

