class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n=set(nums)
        x=list(n)
        if len(nums)!=len(x):
            return True
        else:
            return False
        
