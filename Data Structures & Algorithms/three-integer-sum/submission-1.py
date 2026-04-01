class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        final=[]
        i=0
        while(i<len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                i+=1
                continue
            j=i+1
            k=len(nums)-1
            while(j<k):
                result=nums[i]+nums[j]+nums[k]
                if(result==0):
                    final.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                    while j<k and nums[k]==nums[k+1]:
                        k-=1
                elif result<0:
                    j+=1
                else:
                    k-=1
            i+=1
        return final

        