class Solution:
    def threeSum(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        from itertools import combinations
        k=3
        li=[]
        comb=list(combinations(arr,k))
        x=list(set(comb))
        for i in x:
            if sum(i)==0:
                li.append(list(i))
        return list(li)