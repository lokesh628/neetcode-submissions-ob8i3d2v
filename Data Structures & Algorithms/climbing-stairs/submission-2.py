class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1: return 1
        if n==2: return 2
        n1=1
        n2=2
        for i in range(2,n):
            n3=n2+n1
            n1=n2
            n2=n3
        return n3