class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=curr=0
        n=len(nums)
        mn=float('inf')
        l1=[]
        for r in range(n):
            curr+=nums[r]
            while curr>=target:
                x=r-l+1
                mn=min(mn,x)
                curr-=nums[l]
                l+=1
        return 0 if mn==float('inf') else mn
