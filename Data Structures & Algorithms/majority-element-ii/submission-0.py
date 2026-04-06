class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        x=n//3
        d={}
        l=[]
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        print(d)
        for i,j in d.items():
            if j>x:
                l.append(i)
        return l