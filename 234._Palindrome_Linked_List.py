# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        if not head.next:
            return True
        slow = head
        fast = head.next
        
        stack = [slow.val]
        while fast and fast.next:
            slow = slow.next
            stack.append(slow.val)
            fast = fast.next.next

        if not fast:
            # List is odd, so remove the middle value from stack
            stack.pop()
        
        while len(stack):
            slow = slow.next
            #print(f'Comparing slow.val {slow.val} to stack value {stack[-1]}')
            if slow.val != stack[-1]:
                return False
            stack.pop()
        
        return True