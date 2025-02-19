
class Solution:
	def nthRoot(self, n: int, m: int) -> int:
		# Code here
		start = n
		end = m
		
		while start <= end:
		    mid = (start + end)//2
		    ans = pow(mid, n)
		    
		    if ans == m:
		        return mid
		    if ans > m:
		        end = mid -1
		    if ans < m:
		        start = mid + 1
		        
		return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        m = int(input())
        ob = Solution()
        ans = ob.nthRoot(n, m)
        print(ans)

# } Driver Code Ends