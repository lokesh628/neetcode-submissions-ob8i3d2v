class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            op1=op2=res=0
            if i.lstrip('-').isdigit():
                stack.append(int(i))
            if i=='+':
                op1=stack.pop()
                op2=stack.pop()
                res=op1+op2
                stack.append(res)
            if i=='*':
                op1=stack.pop()
                op2=stack.pop()
                res=op2*op1
                stack.append(res)
            if i=='/':
                op1=stack.pop()
                op2=stack.pop()
                res=op2/op1
                stack.append(int(res))
            if i=='-':
                op1=stack.pop()
                op2=stack.pop()
                res=op2-op1
                stack.append(res)
        return stack[-1]