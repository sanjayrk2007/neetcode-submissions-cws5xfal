class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res=[]
        limit=len(nums)-k+1
        for i in range(limit):
            window=nums[i:i+k]
            res.append(max(window))
        return res