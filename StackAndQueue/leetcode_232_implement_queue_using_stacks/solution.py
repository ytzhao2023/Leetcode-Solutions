class MyQueue(object):

    def __init__(self):
         self.stackA = []
         self.stackB = []
        
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stackA.append(x)

    def pop(self):
        """
        :rtype: int
        """
        while self.stackA:
            # temp only used in this code block.
            temp = self.stackA.pop()
            self.stackB.append(temp)
        ret = self.stackB.pop()
        
        while self.stackB:
            temp = self.stackB.pop()
            self.stackA.append(temp)
        
        return ret

    def peek(self):
        """
        :rtype: int
        """
        while self.stackA:
            temp = self.stackA.pop()
            self.stackB.append(temp)
        ret = self.stackB[-1]
        
        while self.stackB:
            temp = self.stackB.pop()
            self.stackA.append(temp)
        return ret
    def empty(self):
        """
        :rtype: bool
        """
        if len(self.stackA) == 0:
            return True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()