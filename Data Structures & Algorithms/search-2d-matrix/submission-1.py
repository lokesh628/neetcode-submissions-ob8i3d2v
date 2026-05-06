class Solution:
    def searchMatrix(self, arr: List[List[int]], tar: int) -> bool:
        arr1=[]
        for i in arr:
            arr1.extend(i)
        l,h=0,len(arr1)-1
        while(l<=h):
            m=(l+h)//2
            if arr1[m]<tar:
                l=m+1
            elif arr1[m]>tar:
                h=m-1
            else:
                return True
        return False
                