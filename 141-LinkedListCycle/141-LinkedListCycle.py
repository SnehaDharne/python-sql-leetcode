# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # visited = []
        # while head != None:
        #     if head not in visited:
        #         visited.append(head)
        #     else:
        #         return True
        #     head = head.next
        
        # return False

        slow = head
        fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False
        