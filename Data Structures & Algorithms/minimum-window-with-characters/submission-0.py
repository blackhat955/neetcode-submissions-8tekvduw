class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target=Counter(t)

        for freq, value in target.items():
            print(freq, value)

        # let's make the sliding window to find the real window 

        left, right=0, 0 

        need=len(target)
        have=0

        window=defaultdict(int)

        minLen=float('inf')
        res=(-1,-1)

        for right in range(len(s)):
            # what i will do if the window is valid i need to shrink

            if s[right] in target:
                window[s[right]]+=1

                if window[s[right]]==target[s[right]]:
                    have+=1

            # shrink until window is valid


            while need==have:

                windowSize = right - left + 1

                if windowSize<minLen:
                    minLen=windowSize
                    res=(left, right)

                leftChar=s[left]

                if leftChar in target:
                    if window[leftChar]==target[leftChar]:
                        have-=1 
                    window[leftChar]-=1 
                left+=1

        if minLen==float('inf'):
            return ""

        l, r = res

        return s[l:r+1]

            

       

            







