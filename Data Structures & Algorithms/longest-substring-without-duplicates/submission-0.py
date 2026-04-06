class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen=set()
        mx=0
        l=0
        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[i])
            mx=max(mx,i-l+1)
        return mx
