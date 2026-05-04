class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1,n2=len(s1),len(s2)
        if(n1>n2):
            return False
        count1,count2=[0]*26,[0]*26
        for i in range(n1):
            count1[ord(s1[i])-ord('a')]+=1
        for j in range(n2):
            count2[ord(s2[j])-ord('a')]+=1
            if j>=n1:
                count2[ord(s2[j-n1])-ord('a')]-=1
            if count1==count2:
                return True
        return False
        