class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a=[]
        for i in digits:
            a.append(str(i))
        y=''.join(a)
        z=int(y)+1
        a=list(str(z))
        return a