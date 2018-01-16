"""
726. Number of Atoms

Given a chemical formula (given as a string), return the count of each atom.

An atomic element always starts with an uppercase character, then zero or more lowercase letters, representing the name.

1 or more digits representing the count of that element may follow if the count is greater than 1. If the count is 1, no digits will follow. For example, H2O and H2O2 are possible, but H1O2 is impossible.

Two formulas concatenated together produce another formula. For example, H2O2He3Mg4 is also a formula.

A formula placed in parentheses, and a count (optionally added) is also a formula. For example, (H2O2) and (H2O2)3 are formulas.

Given a formula, output the count of all elements as a string in the following form: the first name (in sorted order), followed by its count (if that count is more than 1), followed by the second name (in sorted order), followed by its count (if that count is more than 1), and so on.

Example 1:
Input: 
formula = "H2O"
Output: "H2O"
Explanation: 
The count of elements are {'H': 2, 'O': 1}.
Example 2:
Input: 
formula = "Mg(OH)2"
Output: "H2MgO2"
Explanation: 
The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.
Example 3:
Input: 
formula = "K4(ON(SO3)2)2"
Output: "K4N2O14S4"
Explanation: 
The count of elements are {'K': 4, 'N': 2, 'O': 14, 'S': 4}.
Note:

All atom names consist of lowercase letters, except for the first character which is uppercase.
The length of formula will be in the range [1, 1000].
formula will only consist of letters, digits, and round parentheses, and is a valid formula as defined in the problem.

"""
# LUP Solution
# Open bracket - We push a new dictionary onto a stack to keep track of the atoms and its count in this current group
# Close bracket - The next token might be a number/count. Check whether if it is a count. If it is, multiply all the atoms at the top of the stack by the count and combine it with a dictionary below it in the stack.
# Normal atom - The next token might be a number/count. Check whether if it is a count. If it is, add that atom and its count to the top of the stack.

from collections import defaultdict


class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        tokens = filter(lambda x: x, re.split("([A-Z]{1}[a-z]?|\d+|\(|\))", formula))
        print tokens
        result, i = [defaultdict(int)], 0

        while i < len(tokens):
            token = tokens[i]
            if token == "(":
                result.append(defaultdict(int))

            else:
                counter = 1
                if i + 1 < len(tokens) and re.search("\d+", tokens[i + 1]):
                    counter = int(tokens[i + 1])
                    i += 1
                current = result.pop() if token == ")" else {token: 1}
                for key, value in current.iteritems():
                    result[-1][key] += value * counter

            i += 1

        return "".join([element + (str(count) if count > 1 else '') for element, count in sorted(result[-1].items())])