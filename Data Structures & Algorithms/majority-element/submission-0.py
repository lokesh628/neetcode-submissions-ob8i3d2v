class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        mx=0
        for i,j in d.items():
            if mx<j:
                mx=j
        for i,j in d.items():
            if j==mx:
                return i