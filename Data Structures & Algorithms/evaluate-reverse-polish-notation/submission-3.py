class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in range(len(tokens)):
            print(stack)
            
            
            if tokens[i]=="+":
                stack.append(stack.pop()+stack.pop())
            elif tokens[i]=="-":
                op1,op2=stack.pop(),stack.pop()
                stack.append(op2-op1)
            elif tokens[i]=="*":
                stack.append(stack.pop()*stack.pop())
            elif tokens[i]=="/":
                op1,op2=stack.pop(),stack.pop()
                stack.append(int(float(op2)/op1))
            else:
                stack.append(int(tokens[i]))
        return stack[0]