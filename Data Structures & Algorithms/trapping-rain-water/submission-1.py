class Solution:
    def trap(self, height: List[int]) -> int:
        # n = len(height)
        # prefixMax = [0] * n
        # suffixMax = [0] * n

        # prefixMax[0] = height[0]
        # suffixMax[n-1] = height[n-1]

        # for i in range(1, n):
        #     prefixMax[i]=max(prefixMax[i-1],height[i])

        # for i in range(n-2,-1,-1):
        #     suffixMax[i]=max(suffixMax[i+1], height[i])

        # total=0

        # for i in range(n):
        #     if(height[i]<prefixMax[i] and  height[i]<suffixMax[i]):
        #         total+=min(prefixMax[i], suffixMax[i])-height[i]
        
        # return total

        n=len(height)

        left,right=0, n-1

        total=0

        leftmax=0
        rightmax=0

        while left<right:

            if height[left]<height[right]:
                if height[left]>=leftmax:
                    leftmax=height[left]
                else:
                    total+=leftmax-height[left]
                left+=1
            else:
                if height[right]>=rightmax:
                    rightmax=height[right]
                else:
                    total+=rightmax-height[right]
                right-=1

        return total



        