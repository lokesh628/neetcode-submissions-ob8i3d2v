class Solution:
    def reverseBits(self, n: int) -> int:
        x=f"{n:032b}"
        y=x[::-1]
        return int(y,2)
