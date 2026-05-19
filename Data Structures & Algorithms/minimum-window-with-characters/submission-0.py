class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d={}
        for i in t:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        d1={}
        c=len(t)
        l=0
        mn=float('inf')
        res=''
        for i in range(len(s)):
            if s[i] not in d1:
                d1[s[i]]=1
            else:
                d1[s[i]]+=1
            if s[i] in d and d1[s[i]]<=d[s[i]]:
                c-=1
            while c==0:
                if i-l+1<mn:
                    mn=i-l+1
                    res=s[l:i+1]
                d1[s[l]]-=1
                if s[l] in d and d1[s[l]]<d[s[l]]:
                    c+=1
                l+=1
        return res