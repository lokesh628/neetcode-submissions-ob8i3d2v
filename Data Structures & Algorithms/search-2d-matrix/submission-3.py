class Solution:
    def searchMatrix(self, arr: List[List[int]], tar: int) -> bool:
        m,n=len(arr),len(arr[0])
        r,c=0,n-1
        while r<m and c>=0:
            if arr[r][c]>tar:
                c-=1
            elif arr[r][c]<tar:
                r+=1
            else:
                return True
        return False