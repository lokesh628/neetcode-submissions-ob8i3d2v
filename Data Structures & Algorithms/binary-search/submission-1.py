class Solution:
    def search(self, nums: List[int], tar: int) -> int:
        l=0
        h=len(nums)-1
        while(l<=h):
            m=(l+h)//2
            if nums[m]==tar:
                return m
            elif nums[m]<tar:
                l=m+1
            else:
                h=m-1
        return -1
