class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxdiff=0
        i=0
        j=1
        while(j<len(prices)):
            currdiff=0
            if(prices[i]<prices[j]):
                currdiff=prices[j]-prices[i]
                maxdiff=max(maxdiff,currdiff)
            else:
                i=j
            j+=1
        return maxdiff
            
            