class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        res=[]
        x=list(s)
        y=list(t)
        for i in x:
            if len(x)>=len(y):
                if i in y:
                    res.append(i)
                    y.remove(i)
        a="".join(map(str,res))
        if a==s:
            return True
        else:
            return False