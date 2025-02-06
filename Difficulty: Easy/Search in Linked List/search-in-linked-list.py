#User function Template for python3


''' Node of a linked list

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Solution:
    def searchKey(self, n, head, key):
        #Code here
        if head == None:
            return False
        curr = head
        while True:
            if curr.data == key:
                return True
            else:
                if curr.next == None:
                    break
                else:
                    curr = curr.next
        
        return False


#{ 
 # Driver Code Starts
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        data = list(map(int, input().strip().split()))
        head = Node(data[0])
        tail = head
        for i in range(1, n):
            tail.next = Node(data[i])
            tail = tail.next
        key = int(input())
        ob = Solution()
        res = ob.searchKey(n, head, key)
        key = 0
        if res == True:
            print("true")
        else:
            print("false")

        print("~")

# } Driver Code Ends