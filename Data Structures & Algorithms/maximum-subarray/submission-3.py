class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr=0
        mx=float('-inf')
        for i in range(0,len(nums)):
            curr+=nums[i]
            mx=max(curr,mx)
            if curr<0:
                curr=0
        return mx