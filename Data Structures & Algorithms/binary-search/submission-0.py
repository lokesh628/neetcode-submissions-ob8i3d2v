class Solution:
    def search(self, nums: List[int], tar: int) -> int:
        for i in range(0,len(nums)):
            if nums[i]==tar:
                return i
        return -1