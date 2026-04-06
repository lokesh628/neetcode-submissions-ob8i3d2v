class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res=0
        arr=set(nums)
        for i in nums:
            s=0
            c=i
            while c in arr:
                s=s+1
                c=c+1
            res=max(res,s)
        return res

