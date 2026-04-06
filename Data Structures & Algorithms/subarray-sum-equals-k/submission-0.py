class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        curr=0
        d={}
        l=[]
        c=0
        for i in range(n):
            curr+=nums[i]
            if curr==k:
                c+=1
            if curr-k in d:
                c+=d[curr-k]
            if curr not in d:
                d[curr]=1
            else:
                d[curr]+=1
        return c

