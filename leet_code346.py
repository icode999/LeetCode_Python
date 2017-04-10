"""
346. Moving Average from Data Stream

Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

For example,
MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3

Hide Company Tags Google
Show Tags
"""
from collections import deque
class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.deque = deque([], maxlen=size)
        self.summ = 0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.deque) == self.deque.maxlen:
            self.summ -= self.deque.popleft()
        self.deque.append(val)
        self.summ += val

        return float(self.summ)/len(self.deque)



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)



# LUP

class MovingAverage(object):

    def __init__(self, size):
        self.vect, self.sums, self.idx, self.size = [0] * size, 0, 0, size


    def next(self, val):
        self.idx += 1
        self.sums -= self.vect[self.idx % self.size]
        self.vect[self.idx % self.size] = val
        self.sums += val
        return self.sums / float(min(self.idx, self.size))
