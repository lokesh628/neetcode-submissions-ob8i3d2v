class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pref=1
        suffx=1
        mx=float('-inf')
        n=len(nums)
        for i in range(0,n):
            pref=pref*nums[i]
            suffx=suffx*nums[n-i-1]
            mx=max(mx,pref,suffx)
            if pref==0:
                pref=1
            if suffx==0:
                suffx=1
        return mx