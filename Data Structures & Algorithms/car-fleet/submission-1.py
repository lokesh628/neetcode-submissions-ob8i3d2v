class Solution:
    def carFleet(self, target: int, arr1: List[int], arr2: List[int]) -> int:
        l=[]
        for i in range(len(arr1)):
            x=(target-arr1[i])/arr2[i]
            l.append(x)
        pairs=[]
        for i in range(len(arr1)):
            pairs.append((arr1[i],l[i]))
        pairs.sort()
        n=len(pairs)
        stack=[]
        fleet=0
        for i in range(n-1,-1,-1):
            if not stack or pairs[i][1]>stack[-1]:
                fleet+=1
                stack.append(pairs[i][1])
        return fleet