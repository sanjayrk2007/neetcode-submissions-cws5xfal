class Solution:
    def maxArea(self, heights: List[int]) -> int:
        currArea=-1
        maxArea=-1
        i=0
        j=len(heights)-1
        while(i<j):
            currArea=(j-i)*(min(heights[i],heights[j]))
            maxArea=max(currArea,maxArea)
            if(heights[i]<=heights[j]):i+=1
            else:j-=1
            
        return maxArea

        