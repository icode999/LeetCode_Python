"""
341. Flatten Nested List Iterator

Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:
Given the list [[1,1],2,[1,1]],

By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].

Example 2:
Given the list [1,[4,[6]]],

By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].

Hide Company Tags Google Facebook Twitter
Show Tags
Show Similar Problems

"""

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """


# My Solution
class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        if not nestedList:
            self.stack = list()
        self.stack_iterator = [iter(nestedList)]
        self.next_num = None

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            result = self.next_num
            self.next_num = None
            return result

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.next_num != None:
            return True
        else:
            while len(self.stack_iterator) != 0:
                try:
                    ni = self.stack_iterator[-1].next()
                    #print self.stack_iterator, ni, ni.isInteger()
                    if ni.isInteger():
                        self.next_num = ni.getInteger()
                        #print self.next_num
                        return True
                    else:
                        self.stack_iterator.append(iter(ni.getList()))
                except Exception:
                    self.stack_iterator.pop()

            return False


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())