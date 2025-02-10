# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        cur = head
        cnt = 0
        while cur != None:
            cnt +=1
            cur = cur.next
        k = k % cnt
        print(k)
        for i in range(k):
            curr = head
            while curr and curr.next and curr.next.next:
                    curr = curr.next
            last = curr.next
            last.next = head
            head = last
            curr.next = None

        return head
    