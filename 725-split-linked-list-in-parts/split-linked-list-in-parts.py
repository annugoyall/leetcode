# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def len_LL(self, head):
        if not head:
            return 0
        return 1 + self.len_LL(head.next)


    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n = self.len_LL(head)
        num_elements = n//k
        ans = []
        elements_left = n - num_elements*k

        elements_to_append = num_elements

        def helper(n, head):
            curr_head = head
            ans.append(head)
            while head and n:
                if n == 1:
                    temp = head.next
                    head.next = None
                    head = temp
                    break
                head = head.next
                n -= 1
            return head

        while head:
            if elements_left:
                elements_to_append += 1
                elements_left -= 1
            head = helper(elements_to_append, head)
            elements_to_append = num_elements
        
        curr_arr_size = len(ans)
        for i in range(curr_arr_size, k):
            ans.append(None)

        return ans