#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

    
class Solution:
    def merge(self,l,r,mid,arr):
        s = arr[l:mid+1]
        s2 = arr[mid+1:r+1]
        a1 = 0
        a2 = 0
        k=l
        while a1 < len(s) and a2 < len(s2):
            if s[a1] < s2[a2]:
                arr[k]=s[a1]
                a1+=1
            else:
                arr[k]=s2[a2]
                a2+=1
            k+=1
        while a1 < len(s):
            arr[k] = s[a1]
            a1+=1
            k+=1
        while a2 < len(s2):
            arr[k] = s2[a2]
            a2+=1
            k+=1
            
        return arr

    def mergeSort(self,arr, l, r):
        #code here
        if (l<r):
            mid = (l + r) //2
            self.mergeSort(arr, l, mid)
            self.mergeSort(arr, mid+1, r)
            self.merge(l,r,mid,arr)
        else:
            return

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ob.mergeSort(arr,0,len(arr)-1)
        print(*arr)
        print("~")
        t -= 1


# } Driver Code Ends