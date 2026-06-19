class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            if token not in "+-*/":
                # It's a number, push to stack
                stack.append(int(token))
            else:
                # It's an operator, pop the two operands
                b = stack.pop() # The first popped is the second operand
                a = stack.pop() # The second popped is the first operand
                
                # Perform the operation
                if token == '+': stack.append(a + b)
                elif token == '-': stack.append(a - b)
                elif token == '*': stack.append(a * b)
                elif token == '/': 
                    # Use int(a/b) to truncate toward zero
                    stack.append(int(a / b))
                    
        return stack[0]