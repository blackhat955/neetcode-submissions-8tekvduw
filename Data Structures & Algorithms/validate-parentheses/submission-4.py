class Solution:
    def isValid(self, s: str) -> bool:

        stack=[]

        for ch in s:
            if ch=='(':
                stack.append(')')
            elif ch=='[':
                stack.append(']')
            elif ch=='{':
                stack.append('}')
            else:
                if not stack or stack.pop()!=ch:
                    return False
            
        if len(stack)==0:
            return True
        else:
            return False
        