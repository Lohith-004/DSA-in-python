# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        if head is None or head.next is None:
            return True

        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        second_half = self.reverse(slow)

        first = head
        second = second_half

        while second is not None:
            if first.val != second.val:
                return False
            
            first = first.next
            second = second.next
        
        return True

    def reverse(self, head):
        prev = None
        current = head

        while current is not None:
            next_node = current.next

            current.next = prev
            prev = current

            current = next_node

        return prev