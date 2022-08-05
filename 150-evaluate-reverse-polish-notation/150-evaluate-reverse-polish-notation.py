'''
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6


stack = [6]
if elem.isdigit():
    stack.add(elem)
else:
    operand_two = int( stack.pop() )
    operand_one = int( stack.pop() )
    
    if elem == "+":
        eval = operand_one + operand_two
    elif elem == "-":
        eval = operand_one - operand_two
    elif elem == "/":
        eval = operand_one // operand_two
    elif elem == "*":
        eval = operand_one * operand_two
    stack.add(eval)
    
return stack.top()
'''

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for item in tokens:
            if item != "+" and item != "-" and item != "/" and item !="*":
                stack.append(item)
            else:
                operand_two = int(stack.pop())
                operand_one = int(stack.pop())
                if item == "+": evaluate = int(operand_one + operand_two)
                if item == "-": evaluate = int(operand_one - operand_two)
                if item == "*": evaluate = int(operand_one * operand_two)
                if item == "/": evaluate = int(operand_one / operand_two)
                stack.append(evaluate)
        print(stack)
        return stack[-1]
        
        