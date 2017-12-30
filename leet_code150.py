"""
150. Evaluate Reverse Polish Notation

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6

Companies 
LinkedIn

"""
# MOWN using stack
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = list()
        for token in tokens:
            if token in ["+", "-", "*", "/"]:
                b = stack.pop()
                a = stack.pop()

                if token == "+":
                    stack.append(a + b)

                elif token == "-":
                    stack.append(a - b)

                elif token == "*":
                    stack.append(a * b)

                # here take care of the case like "1/-22",
                # in Python 2.x, it returns -1, while in
                # Leetcode it should return 0
                else:
                    stack.append(int(float(a) / float(b)))
            else:
                stack.append(int(token))

        return stack[-1]
