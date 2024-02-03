class MyStack(object):

    def __init__(self):
        self.queue = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue.append(x)

    def pop(self):
        """
        :rtype: int
        """
        for i in range(len(self.queue)-1):
            temp = self.queue.pop()
            self.queue.append(temp)
        res = self.queue.pop()
        return res    
        

    def top(self):
        """
        :rtype: int
        """
        for i in range(len(self.queue)-1):
            temp = self.queue.pop()
            self.queue.append(temp)
        res = self.queue.pop()
        self.queue.append(res)
        return res  
        

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.queue == 0):
            return True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()