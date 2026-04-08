class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=s.lower()
        res=""
        for char in a:
            if char.isalnum() or char=='':
                res+=char
        x=list(res)
        l,r=0,len(x)-1
        while l<r:
            if x[l]!=x[r]:
                return False
            l+=1
            r-=1
        return True