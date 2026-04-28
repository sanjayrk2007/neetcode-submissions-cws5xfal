class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:return 0
        seen=list(set(nums))
        seen.sort()
        longest=1
        count=1
        for i in range(1,len(seen)):
            if((seen[i]-seen[i-1])==1):
                count+=1
                longest=max(longest,count)
            else:
                count=1
        return longest
