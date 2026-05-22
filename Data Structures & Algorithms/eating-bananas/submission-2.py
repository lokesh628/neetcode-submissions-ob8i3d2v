class Solution:
    def minEatingSpeed(self, arr: List[int], target: int) -> int:
        mn=float('inf')
        l=1
        h=max(arr)
        while l<=h:
            mid=(l+h)//2
            s=0
            for i in range(len(arr)):
                s+=math.ceil(arr[i]/mid)
            if s<=target:
                mn=min(mn,mid)
                h=mid-1
            else:
                l=mid+1
        return mn