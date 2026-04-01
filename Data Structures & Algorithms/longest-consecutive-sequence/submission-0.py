class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:return 0
        unique_list=list(set(nums))
        unique_list.sort()
        n=len(unique_list)
        count=1
        longest=1
        for i in range(1,n):
            if ((unique_list[i]-unique_list[i-1])==1):
                count+=1
                longest=max(longest,count)
            else:
                count=1
        return longest