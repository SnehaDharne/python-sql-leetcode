# Last updated: 4/7/2025, 8:31:40 PM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        curr = head
        if not head or not head.next:
            return None
        count = 0
        while curr is not None:
            count+=1
            curr = curr.next
        n = count - n
        print(n)
        curr = head
        if n == 0:
            head = head.next
            return head
        for i in range(n-1):
            curr = curr.next
            print(curr)
        curr.next = curr.next.next

        return head
        
        