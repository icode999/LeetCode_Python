"""
621. Task Scheduler

Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks.Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.

Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
Note:
The number of tasks is in the range [1, 10000].
The integer n is in the range [0, 100].

Companies
Facebook
"""
# LUP Solution
# Create a 26 array
# Basic idea is to start dealing with most frequent task
# For example: A: 100, B : 99, C: 98 and n = 1
# A->B->A->B->A->C->B (look at the sequence after B is executed twice (current count 97), its not frequent than C, hence C gets executed)

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        task_list = [0] * 26
        for task in tasks:
            task_list[ord(task) - ord('A')] += 1

        task_list.sort(reverse=True)
        result = 0

        while task_list[0]:
            current, need_cool = 0, n + 1
            while current <= n and task_list[current]:
                task_list[current] -= 1
                result += 1
                current += 1
                need_cool -= 1

            if task_list[0]:
                result += need_cool
            task_list.sort(reverse=True)

        return result
