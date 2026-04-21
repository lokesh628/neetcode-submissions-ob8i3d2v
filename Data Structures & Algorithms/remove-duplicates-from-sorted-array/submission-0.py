class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        d={}
        c=0
        n=len(nums)
        for i in nums:
            if i not in d:
                d[i]=1
                nums[c]=i
                c+=1
            else:
                d[i]+=1
        return c
