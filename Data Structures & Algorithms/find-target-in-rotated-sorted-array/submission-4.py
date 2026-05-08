class Solution:
    def search(self, nums: List[int], tar: int) -> int:
        l,h=0,len(nums)-1
        while l<=h:
            mid=(l+h)//2
            if nums[mid]==tar:
                return mid
            if nums[mid]>=nums[l]:
                if tar>nums[mid] or tar<nums[l]:
                    l=mid+1
                else:
                    h=mid-1
            else:
                if tar<nums[mid] or tar>nums[h]:
                    h=mid-1
                else:
                    l=mid+1
        return -1