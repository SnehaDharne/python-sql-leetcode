def Fibo(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    else:
        return(Fibo(n-1) + Fibo(n-2))

class Solution:
    def fib(self, n: int) -> int:
        return Fibo(n)
