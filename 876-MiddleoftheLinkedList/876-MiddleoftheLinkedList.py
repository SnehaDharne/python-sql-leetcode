# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        curr2 = head
        if head.next == None:
            return head
        while True:
            curr = curr.next
            curr2 = curr2.next.next

            if curr2 == None or curr2.next == None:
                return curr