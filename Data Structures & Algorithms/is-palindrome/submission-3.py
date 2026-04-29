class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1=""
        for c in s:
            if c.isalnum():
                s1+=c

        i=0
        j=len(s1)-1
        while(i<j):
            if(s1[i].lower()!=s1[j].lower()):
                return False
            else:
                i+=1
                j-=1
        return True
