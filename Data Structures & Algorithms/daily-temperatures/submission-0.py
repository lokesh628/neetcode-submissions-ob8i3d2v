class Solution:
    def dailyTemperatures(self, arr: List[int]) -> List[int]:
        n=len(arr)
        stack=[]
        n=len(arr)
        stack=[]
        res=[0]*n
        for i in range(n):
            while stack and arr[i]>stack[-1][0]:
                res[stack[-1][1]]=abs(stack[-1][1]-i)
                stack.pop()
            stack.append((arr[i],i))
        return res