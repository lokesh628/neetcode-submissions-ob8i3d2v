class Solution:
    def maxArea(self, arr: List[int]) -> int:
        i=0
        j=len(arr)-1
        mx=0
        while(i<j):
            area=min(arr[i],arr[j])*(abs(i-j))
            mx=max(mx,area)
            if arr[i]<arr[j]:
                i+=1
            else:
                j-=1
        return mx