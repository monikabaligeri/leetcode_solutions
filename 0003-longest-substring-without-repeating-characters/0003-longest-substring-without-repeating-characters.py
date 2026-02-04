class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max1=0
        left=0
        uniqset=set()
        for right in range(0,len(s)):
                while s[right]in uniqset:
                    uniqset.remove(s[left])
                    left+=1
                uniqset.add(s[right])
                max1=max(max1,right-left+1)
        return max1