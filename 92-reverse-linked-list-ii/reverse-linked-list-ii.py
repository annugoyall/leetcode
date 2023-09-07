# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def find(self, head, n):
        if n == 1:
            return None, head
        
        if n == 2:
            return head, head.next
        
        return self.find(head.next, n-1)

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        pre1, node1 = self.find(head, left)
        pre2, node2 = self.find(head, right)

        if not node1 or not node2:
            return head

        next_node2 = node2.next
        node2.next = None

        pre = None
        curr = node1

        while curr:
            temp = curr.next
            curr.next = pre
            pre, curr = curr, temp

        if pre1:
            pre1.next = pre
        else:
            head = pre
        node1.next = next_node2

        return head