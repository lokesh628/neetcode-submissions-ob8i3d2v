class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=s.lower()
        res=""
        for char in a:
            if char.isalnum() or char=='':
                res+=char
        x=list(res)
        li=[]
        l=0
        h=len(x)-1
        while(l<h):
            x[l]=x[h]
            x[h]=x[l]
            l+=1
            h-=1
        li=x
        y="".join(li)
        if(y==res):
            return True
        else:
            return False