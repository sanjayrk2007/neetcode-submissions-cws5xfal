class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1=len(s1)
        n2=len(s2)
        for i in range(n2-n1+1):
            string_1=s2[i:i+n1]
            string1_sort="".join(sorted(string_1))
            string2_sort="".join(sorted(s1))
            if(string1_sort==string2_sort):
                return True
        return False
            

        