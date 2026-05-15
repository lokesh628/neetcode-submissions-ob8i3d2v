class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,h=0,len(nums)-1
        mn=nums[0]
        while l<=h:
            if nums[l]<nums[h]:
                mn=min(mn,nums[l])
                break
            mid=(l+h)//2
            if nums[mid]>=nums[l]:
                l=mid+1
                mn=min(mn,nums[mid])
            else:
                h=mid-1
                mn=min(mn,nums[mid])
        return mn
