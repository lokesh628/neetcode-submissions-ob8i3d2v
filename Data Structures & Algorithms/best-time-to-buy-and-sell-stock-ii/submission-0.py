class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        l=[]
        s=0
        for i in range(1,n):
            x=prices[i]-prices[i-1]
            l.append(x)
        for i in l:
            if i>0:
                s+=i
        return s