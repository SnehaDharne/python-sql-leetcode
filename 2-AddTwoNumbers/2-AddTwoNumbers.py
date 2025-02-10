# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        current = dummyHead
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        carry = 0
        sum1 = 0
        while l1 or l2 or carry:
            sum1 = carry
            if l1:
                sum1 = l1.val + sum1
                l1 = l1.next
            if l2:
                sum1 = l2.val + sum1
                l2 = l2.next
            carry = 0

            dig = sum1 % 10
            carry = sum1 // 10
            current.next = ListNode(dig, None)
            current = current.next
            
        result = dummyHead.next
        return result

        
