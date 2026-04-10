class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False

        left=0

        n=len(s1)

        count=[0]*26


        for val in s1:
            count[ord(val)-ord('a')]+=1

        for right in range(len(s2)):

            count[ord(s2[right])-ord('a')]-=1

            if right-left+1>n:
                # if i to make the count at all position 0 then
                # which mean it has valid permutation
                
                # i want to checj her if count is all 0 
                # not then i want to increase left
                 count[ord(s2[left]) - ord('a')] += 1
                 left += 1

            if count == [0] * 26:
                return True

        return False

        

            
            



