class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n=len(nums)
        c=0
        while c<k:
            x=max(nums)
            nums.remove(x)
            c=c+1
        return x