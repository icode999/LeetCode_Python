"""
729. My Calendar I

Implement a MyCalendar class to store your events. A new event can be added if adding the event will not cause a double booking.

Your class will have the method, book(int start, int end). Formally, this represents a booking on the half open interval [start, end), the range of real numbers x such that start <= x < end.

A double booking happens when two events have some non-empty intersection (ie., there is some time that is common to both events.)

For each call to the method MyCalendar.book, return true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.

Your class will be called like this: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)
Example 1:
MyCalendar();
MyCalendar.book(10, 20); // returns true
MyCalendar.book(15, 25); // returns false
MyCalendar.book(20, 30); // returns true
Explanation:
The first event can be booked.  The second can't because time 15 is already booked by another event.
The third event can be booked, as the first event takes every time less than 20, but not including 20.
Note:

The number of calls to MyCalendar.book per test case will be at most 1000.
In calls to MyCalendar.book(start, end), start and end are integers in the range [0, 10^9].

Companies
Google

"""
# MOWN BruteForce
class MyCalendar:
    def __init__(self):
        self.intervals = []

    def book(self, start, end):
        for s, e in self.intervals:
            if not (start >= e or end <= s): return False
        self.intervals.append((start, end))
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)

# LUP BST

class Node(object):
    def __init__(self, s, e):
        self.start = s
        self.end = e
        self.left = None
        self.right = None


class MyCalendar:
    def __init__(self):
        self.root = None

    def book_helper(self, node, start, end):
        if start >= node.end:
            if node.right:
                return self.book_helper(node.right, start, end)
            else:
                node.right = Node(start, end)
                return True

        elif end <= node.start:
            if node.left:
                return self.book_helper(node.left, start, end)
            else:
                node.left = Node(start, end)
                return True
        else:
            return False

    def book(self, start, end):
        if not self.root:
            self.root = Node(start, end)
            return True

        return self.book_helper(self.root, start, end)

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
