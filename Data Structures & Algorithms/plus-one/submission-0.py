class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x=[i for num in digits for i in str(num)]
        y=''.join(x)
        z=int(y)+1
        a=list(str(z))
        return a