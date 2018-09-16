"""
904. Fruit Into Baskets

In a row of trees, the i-th tree produces fruit with type tree[i].

You start at any tree of your choice, then repeatedly perform the following steps:

Add one piece of fruit from this tree to your baskets.  If you cannot, stop.
Move to the next tree to the right of the current tree.  If there is no tree to the right, stop.
Note that you do not have any choice after the initial choice of starting tree: you must perform step 1, then step 2, then back to step 1, then step 2, and so on until you stop.

You have two baskets, and each basket can carry any quantity of fruit, but you want each basket to only carry one type of fruit each.

What is the total amount of fruit you can collect with this procedure?



Example 1:

Input: [1,2,1]
Output: 3
Explanation: We can collect [1,2,1].
Example 2:

Input: [0,1,2,2]
Output: 3
Explanation: We can collect [1,2,2].
If we started at the first tree, we would only collect [0, 1].
Example 3:

Input: [1,2,3,2,2]
Output: 4
Explanation: We can collect [2,3,2,2].
If we started at the first tree, we would only collect [1, 2].
Example 4:

Input: [3,3,3,1,2,1,1,2,3,3,4]
Output: 5
Explanation: We can collect [1,2,1,1,2].
If we started at the first tree or the eighth tree, we would only collect 4 fruits.


Note:

1 <= tree.length <= 40000
0 <= tree[i] < tree.length

"""

# MOWN With 2 Bugs
class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        last1, last2, result = 0, 0, 0
        i, current1, current2, current = 0, None, None, 0
        while i < len(tree):
            # print tree[i], current1, current2, current, result

            if current1 == None:
                current1 = tree[i]
                current += 1
                last1 = i

            elif current1 != tree[i] and current2 == None:  # Bug1 check if current1 == tree[i] [1, 1, 0, 0]
                current2 = tree[i]
                current += 1
                last2 = i

            elif tree[i] in [current1, current2]:
                if tree[i] == current1:
                    last1 = i

                else:
                    last2 = i

                current += 1

            else:
                if current:
                    result = max(result, current)

                if last1 < last2:  # Bug2 Took the least one always [1,0,1,4,1,4,1,2,3]
                    i = last1 + 1
                else:
                    i = last2 + 1

                current1 = tree[i]
                last1 = i
                current2 = None
                current = 1
            i += 1

        if current:
            result = max(result, current)

        return result

