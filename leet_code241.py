"""
241. Different Ways to Add Parentheses

Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.


Example 1
Input: "2-1-1".

((2-1)-1) = 0
(2-(1-1)) = 2
Output: [0, 2]


Example 2
Input: "2*3-4*5"

(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10
Output: [-34, -14, -10, -10, 10]

Credits:
Special thanks to @mithmatt for adding this problem and creating all test cases.

Hide Tags Divide and Conquer
Hide Similar Problems
"""
class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]

        Solution: Devide and conquer
        final solution = solution(input[:i]) operator solutin(input[i+1:])
        """
        if input.isdigit():
            return [int(input)]

        result = list()
        for i in range(len(input)):
            if input[i] in ['-', '+', '*']:
                sol1, sol2 = self.diffWaysToCompute(input[:i]), self.diffWaysToCompute(input[i+1:])
                result += [eval(str(exp1) + input[i] + str(exp2)) for exp1 in sol1 for exp2 in sol2]
        return result