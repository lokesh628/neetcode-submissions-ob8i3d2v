class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res=''
        stack=[]
        for i in range(len(s)):
            if s[i].isalpha() or s[i]=='(':
                res=res+s[i]
            if s[i]=='(':
                stack.append(s[i])
            elif s[i]==')':
                if '(' in stack:
                    res=res+s[i]
                    stack.pop()
        fin=''
        for i in range(len(res)-1,-1,-1):
            if res[i]=='(' and stack:
                stack.pop()
                continue
            fin=fin+res[i]
        return fin[::-1]
                
                