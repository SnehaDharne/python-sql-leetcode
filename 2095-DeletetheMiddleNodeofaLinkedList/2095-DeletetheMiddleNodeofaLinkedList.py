# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head_copy = head
        fast = head
        if head == None or head.next == None:
            return None
        while fast!= None and fast.next != None:
            copy = head
            head = head.next
            fast = fast.next.next

        copy.next = head.next

        return head_copy