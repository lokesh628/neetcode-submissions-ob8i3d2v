class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn=float('inf')
        mx=0
        for i in range(0,len(prices)):
            mn=min(mn,prices[i])
            mx=max(mx,prices[i]-mn)
        return mx
