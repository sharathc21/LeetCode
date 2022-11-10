class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r= len(height) -1
        
        res =0
        
        while l<r:
            res = max(res, (r-l) * min(height[l], height[r]) )
            if height[l]<height[r] :
                l+=1
            elif height[r]<= height[l]:
                r-=1
            # if l<r :
            #     l+=1
            # elif r<= l:
            #     r-=1
        return res
        