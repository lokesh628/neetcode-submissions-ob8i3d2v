class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l=[]
        n=len(nums)
        for i in range(n-k+1):
            x=max(nums[i:i+k])
            l.append(x)
        return l