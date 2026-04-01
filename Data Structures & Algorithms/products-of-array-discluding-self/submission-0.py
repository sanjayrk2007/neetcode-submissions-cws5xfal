class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        result=[0]*n
        zerocount=0
        product=1
        zeroindex=-1
        for i,num in enumerate(nums):
            if(num==0):
                zerocount+=1
                zeroindex=i
            else:
                product*=num
        if (zerocount>1):return result
        elif (zerocount==1):
            result[zeroindex]=product
            return result
        for i in range(n):
            result[i]=product//nums[i]
        return result
        