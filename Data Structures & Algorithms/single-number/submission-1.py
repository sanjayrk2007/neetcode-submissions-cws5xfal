class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dup=0
        for num in nums:
            dup=num^dup
        return dup