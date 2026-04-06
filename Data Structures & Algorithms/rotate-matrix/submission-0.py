class Solution:
    def rotate(self, m: List[List[int]]) -> None:
        N=list(map(list,zip(*m)))
        for i in N:
            i.reverse()
            m[:]=N