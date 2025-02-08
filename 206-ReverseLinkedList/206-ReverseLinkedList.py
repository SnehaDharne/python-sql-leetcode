# Definition for singly-linked list.
def reverse_func(head):
        if head == None or head.next == None:
            return head
        newHead = reverse_func(head.next)
        front = head.next
        front.next = head
        head.next = None
        return newHead
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # node = None 
        # curr = head
        # if head == None:
        #     return None
        # while curr:
        #     curr_temp = curr.next
        #     curr.next = node
        #     node = curr
        #     curr = curr_temp
        #better approach
        node = reverse_func(head)
        return node