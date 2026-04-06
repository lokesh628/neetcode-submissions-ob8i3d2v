class Solution:
    def searchMatrix(self, arr: List[List[int]], tar: int) -> bool:
        arr1=[]
        for i in arr:
            arr1.extend(i)
        for i in range(0,len(arr1)):
            if arr1[i]==tar:
                return True
        return False
                