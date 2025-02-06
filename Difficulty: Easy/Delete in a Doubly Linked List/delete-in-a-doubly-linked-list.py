class Solution:
    def delete_node(self, head, x):
        #code here
        curr = head
        if x ==1:
            if head != None:
                n = head.next
                n.prev = None
                return n
            else:
                return head
                
        for i in range(1, x):
            curr = curr.next
        
        if curr.next == None:
            prev1 = curr.prev
            prev1.next = None
            return head
            
        else:
            next1 = curr.next
            prev1 = curr.prev
            
            prev1.next = next1
            next1.prev = prev1
            return head
            

#{ 
 # Driver Code Starts
class Node:

    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None


def push(tail, new_data):
    newNode = Node(new_data)
    newNode.next = None
    newNode.prev = tail

    if tail:
        tail.next = newNode

    return newNode


def verifyDLL(head):
    c1, c2 = 0, 0
    tmp = head
    while tmp.next:
        c1 += 1
        tmp = tmp.next
    while tmp.prev:
        c2 += 1
        tmp = tmp.prev
    return c1 == c2


def printList(head):
    if not head:
        return
    if verifyDLL(head) == False:
        return
    while head:
        print(head.data, end=" ")
        head = head.next
    print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        head = Node(arr[0])
        tail = head

        for value in arr[1:]:
            tail = push(tail, value)

        ob = Solution()
        resHead = ob.delete_node(head, int(input().strip()))
        printList(resHead)
        print("~")

# } Driver Code Ends