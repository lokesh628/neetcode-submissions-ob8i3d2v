class Solution:
    def trap(self, height: List[int]) -> int:
        l,h=0,len(height)-1
        lmax=rmax=total=0
        while l<=h:
            if height[l]<=height[h]:
                if lmax<height[l]:
                    lmax=height[l]
                else:
                    total+=lmax-height[l]
                l+=1
            else:
                if rmax<height[h]:
                    rmax=height[h]
                else:
                    total+=rmax-height[h]
                h-=1
        return total