"""
716. Max Stack

Design a max stack that supports push, pop, top, peekMax and popMax.

push(x) -- Push element x onto stack.
pop() -- Remove the element on top of the stack and return it.
top() -- Get the element on the top.
peekMax() -- Retrieve the maximum element in the stack.
popMax() -- Retrieve the maximum element in the stack, and remove it. If you find more than one maximum elements, only remove the top-most one.
Example 1:
MaxStack stack = new MaxStack();
stack.push(5); 
stack.push(1);
stack.push(5);
stack.top(); -> 5
stack.popMax(); -> 5
stack.top(); -> 1
stack.peekMax(); -> 5
stack.pop(); -> 1
stack.top(); -> 5

Note:
-1e7 <= x <= 1e7
Number of operations won't exceed 10000.
The last four operations won't be called when stack is empty.

Companies 
LinkedIn

"""
# LUP Solution using two stack
# for pop max, we need to pop all elements from stack to a temp stack until we hit max element and push them
# back in the same order (make sure in same order)
class MaxStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = list()
        self.max_stack = list()

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if not self.max_stack:
            self.max_stack.append(x)

        else:
            if self.max_stack[-1] <= x:
                self.max_stack.append(x)
        return None

    def pop(self):
        """
        :rtype: int
        """
        current = None
        if self.stack:
            current = self.stack.pop()
            if self.max_stack[-1] == current:
                self.max_stack.pop()

        return current

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]
        else:
            return None

    def peekMax(self):
        """
        :rtype: int
        """
        if self.max_stack:
            return self.max_stack[-1]
        else:
            return None

    def popMax(self):
        """
        :rtype: int
        """
        maxx = self.max_stack.pop()
        current = list()
        while self.stack:
            temp = self.stack.pop()
            if temp == maxx:
                for curr in current[::-1]:
                    self.push(curr)
                break
            else:
                current.append(temp)
        return maxx




        # Your MaxStack object will be instantiated and called as such:
        # obj = MaxStack()
        # obj.push(x)
        # param_2 = obj.pop()
        # param_3 = obj.top()
        # param_4 = obj.peekMax()
        # param_5 = obj.popMax()