class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        if(len(s)%2!=0):
            return False
        for i in range(len(s)):
            if s[i]=='(' or s[i]=='{' or s[i]=='[':
                stack.append(s[i])
            elif s[i]==')' or s[i]=='}' or s[i]==']':
                print(len(stack))
                if len(stack)==0:
                    return False
                if stack[-1]=='(' and s[i]==')':
                    stack.pop()
                elif stack[-1]=='{' and s[i]=='}':
                    stack.pop()
                elif stack[-1]=='[' and s[i]==']':
                    stack.pop()
                else:
                    return False
        if(len(stack)==0):
            return True
        return False
