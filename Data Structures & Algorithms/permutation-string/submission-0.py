class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        x=Counter(s1)
        l=0
        d={}
        for i in range(len(s2)):
            if s2[i] not in d:
                d[s2[i]]=1
            else:
                d[s2[i]]+=1
            while i-l+1>len(s1):
                d[s2[l]]-=1
                if d[s2[l]]==0:
                    del d[s2[l]]
                l+=1
            if x==d:
                return True
        return False