class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        li=[]
        for i in range(n):
            p=1
            for j in range(n):
                if (i==j):
                    continue
                else:
                    p=p*nums[j]
            li.append(p)
        return li
