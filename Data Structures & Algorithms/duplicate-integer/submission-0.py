class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        List2=[]
        duplicate=0
        for num in nums:
            if num not in List2:
                List2.append(num)
            else:
                duplicate=1
                break 
        if duplicate==1:
            return True
        else:
            return False