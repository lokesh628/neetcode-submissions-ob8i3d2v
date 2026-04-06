class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        li=[]
        d={}
        for s in strs:
            x="".join(sorted(s))
            if x not in d:
                d[x]=[s]
            else:
                d[x].append(s)
        res=list(d.values())
        return res
