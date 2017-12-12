"""
170. Two Sum III - Data structure design

Design and implement a TwoSum class. It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

For example,
add(1); add(3); add(5);
find(4) -> true
find(7) -> false

"""
# MOWN but with bugs
from collections import defaultdict

class TwoSum(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = defaultdict(int)

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        self.data[number] += 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        # Bug 1: not checking (value-num != num)  in if condition
        # this will fail ["TwoSum","add","add","add","find"]  and [[],[0],[-1],[1],[0]]
        # Bug 2: Using defaultdict will add key to the dict if someone call mapr[key] which doesnt exist
        # so we have to check if mapr has key or not before calling it
        for num in self.data.keys():
            if self.data.has_key(value-num):
                if (value-num == num and self.data[num] > 1) or (value-num != num):
                    return True
        return False



        # Your TwoSum object will be instantiated and called as such:
        # obj = TwoSum()
        # obj.add(number)
        # param_2 = obj.find(value)