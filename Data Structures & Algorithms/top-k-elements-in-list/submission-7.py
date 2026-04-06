class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        from collections import Counter
        d=Counter(nums)
        most=d.most_common(k)
        li=[]
        for i in most:
            li.append(i[0])
        return li
