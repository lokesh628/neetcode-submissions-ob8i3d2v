class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        freq=Counter(nums)
        most=freq.most_common(k)
        top=[i[0] for i in most]
        return top
