class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        d={}
        arr=[]
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for i,j in d.items():
            arr.append(i)
        l,h=0,len(arr)-1
        while l<=h:
            mid=(l+h)//2
            if arr[mid]==target:
                return True
            if arr[l]<=arr[mid]:
                if arr[l]<=target<arr[mid]:
                    h=mid-1
                else:
                    l=mid+1
            else:
                if arr[mid]<target<=arr[h]:
                    l=mid+1
                else:
                    h=mid-1
        return False