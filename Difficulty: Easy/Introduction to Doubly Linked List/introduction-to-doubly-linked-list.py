#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

'''
# Node Class

'''
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        self.prev = None
class Solution:
    def constructDLL(self, arr):
        # Code here
        start = Node(arr[0])
        current = start
        current.prev = None
        current.next = None
        for i in range(1, len(arr)):
            new_node = Node(arr[i])
            current.next = new_node
            new_node.prev = current
            new_node.next = None
            current = new_node

        return start 

#{ 
 # Driver Code Starts.
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        self.prev = None
def printList(node):
    tmp = node
    if tmp:
        c1, c2 = 0, 0
        while tmp.next:
            c1 += 1
            tmp = tmp.next
        while tmp.prev:
            c2 += 1
            tmp = tmp.prev
        if c1 != c2:
            print("-1")
            return
    while tmp:
        print(tmp.data, end = " ")
        tmp = tmp.next
    print()

if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.constructDLL(arr)
        printList(res)
        print("~")
# } Driver Code Ends