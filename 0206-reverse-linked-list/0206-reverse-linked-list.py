# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            curr = ListNode(head.val)
            head = head.next
            while(head):
                prev = ListNode(head.val)
                prev.next = curr
                curr = prev
                head=head.next
            return curr