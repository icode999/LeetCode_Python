"""
604. Design Compressed String Iterator

Design and implement a data structure for a compressed string iterator. It should support the following operations: next and hasNext.

The given compressed string will be in the form of each letter followed by a positive integer representing the number of this letter existing in the original uncompressed string.

next() - if the original string still has uncompressed characters, return the next letter; Otherwise return a white space.
hasNext() - Judge whether there is any letter needs to be uncompressed.

Note:
Please remember to RESET your class variables declared in StringIterator, as static/class variables are persisted across multiple test cases. Please see here for more details.

Example:

StringIterator iterator = new StringIterator("L1e2t1C1o1d1e1");

iterator.next(); // return 'L'
iterator.next(); // return 'e'
iterator.next(); // return 'e'
iterator.next(); // return 't'
iterator.next(); // return 'C'
iterator.next(); // return 'o'
iterator.next(); // return 'd'
iterator.hasNext(); // return true
iterator.next(); // return 'e'
iterator.hasNext(); // return false
iterator.next(); // return ' '

Companies 
Google 

"""

# MOWN Solution with bug

# Bug: Make sure you handle condition where "L1e2t1C1o1d1e1" can also be "L1e2t1C1o12d1e11"

from re import findall
class StringIterator(object):
    def __init__(self, compressedString):
        """
        :type compressedString: str
        """
        self.compressedString = re.findall("\D\d+", compressedString)
        for i in range(len(self.compressedString)):
            self.compressedString[i] = (self.compressedString[i][0], int(self.compressedString[i][1:]))

        self.current_char, self.current_count, self.index = None, 0, len(self.compressedString)

    def next(self):
        """
        :rtype: str
        """
        if not self.hasNext():
            return " "
        if not self.current_count:
            self.current_char, self.current_count = self.compressedString[-self.index]
            self.index -= 1
        self.current_count -= 1
        return self.current_char

    def hasNext(self):
        """
        :rtype: bool
        """
        return True if self.current_count or self.index else False

        # Your StringIterator object will be instantiated and called as such:
        # obj = StringIterator(compressedString)
        # param_1 = obj.next()
        # param_2 = obj.hasNext()