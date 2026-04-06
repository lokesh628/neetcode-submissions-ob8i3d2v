class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        s=(n*(n+1))//2
        s1=sum(nums)
        z=s-s1
        return z