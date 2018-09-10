"""
399. Evaluate Division

Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0.
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.

According to the example above:

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ].
The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.


Companies
Google 20 Facebook 5
"""
# MOWN with Bug
# DFS graph
from collections import defaultdict
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        mapr = defaultdict(list)
        for idx, eq in enumerate(equations):
            mapr[eq[0]].append([eq[1], values[idx]])
            mapr[eq[1]].append([eq[0], 1 / values[idx]])

        result = list()
        for query in queries:
            if query[0] not in mapr or query[1] not in mapr:
                result.append(-1.0)

            elif query[0] == query[1]:
                result.append(1.0)

            else:
                stack = mapr[query[0]][:]  # Bug if not properly copied, [:] without this, stack.pop effects mapr
                visited = set([query[0]])
                while stack:
                    node = stack.pop()
                    if node[0] in visited:
                        continue

                    visited.add(node[0])
                    if node[0] == query[1]:
                        result.append(node[1])
                        break

                    else:
                        for tnode in mapr[node[0]]:
                            stack.append([tnode[0], tnode[1] * node[1]])
                else:
                    result.append(-1.0)

        return result