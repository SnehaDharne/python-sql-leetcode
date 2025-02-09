# Definition for singly-linked list.
def reverse_list(head):
    if head == None or head.next == None:
        return head
    new_head = reverse_list(head.next)
    front = head.next
    front.next = head
    head.next = None
    return new_head

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        if slow == None or slow.next == None:
            return True
        if slow.next.next == None:
            return (slow.val == slow.next.val)
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
        second_half = slow.next
        slow.next = None
        end_head = reverse_list(second_half)
        slow = head
        
        while end_head != None:
            if slow.val != end_head.val:
                reverse_list(end_head)
                return False

            slow = slow.next
            end_head = end_head.next
                

        reverse_list(end_head)
        return True
        
       
       



