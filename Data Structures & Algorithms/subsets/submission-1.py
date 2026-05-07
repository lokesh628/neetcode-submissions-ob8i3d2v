class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        n=len(nums)
        for i in range(1<<n):
            l=[]
            for j in range(n):
                if i & (1<<j):
                    l.append(nums[j])
            res.append(l)
        return res