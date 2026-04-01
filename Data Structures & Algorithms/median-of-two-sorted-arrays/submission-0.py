class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m=nums1+nums2
        m.sort()
        totalLen=len(m)
        ans=1.0
        if totalLen % 2 == 0:
            return (m[totalLen // 2 - 1] + m[totalLen // 2]) / 2.0
        else:
            return m[totalLen // 2]
        return ans
            
            