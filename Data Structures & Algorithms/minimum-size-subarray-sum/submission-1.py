class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=curr=0
        n=len(nums)
        mn=float('inf')
        l1=[]
        for r in range(n):
            curr+=nums[r]
            while curr>=target:
                l1.append(nums[l:r+1])
                curr-=nums[l]
                l+=1
        for i in l1:
            if len(i)<mn:
                mn=len(i)
        return 0 if mn==float('inf') else mn
