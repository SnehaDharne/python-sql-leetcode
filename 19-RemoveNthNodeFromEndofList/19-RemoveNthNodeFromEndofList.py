# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverse_list(head):
    if head == None or head.next == None:
        return head

    new_head = reverse_list(head.next)
    front = head.next
    front.next = head
    head.next = None

    return new_head


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if head == None:
            return head
        elif head.next == None:
            if n == 1:
                return None


        back = reverse_list(head)
        end = back
        prev = back

        if n == 1:
            return reverse_list(back.next)

        for i in range(1,n):
            prev = back
            back = back.next
        
        if back.next:
            prev.next = back.next
        else:
            prev.next = None

        return reverse_list(end)
