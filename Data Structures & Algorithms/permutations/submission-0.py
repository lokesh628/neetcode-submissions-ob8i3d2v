class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        sol,ans=[],[]
        n=len(nums)
        def backtrack():
            if len(sol)==n:
                ans.append(sol[:])
                return
            for i in nums:
                if i not in sol:
                    sol.append(i)
                    backtrack()
                    sol.pop()
        backtrack()
        return ans

