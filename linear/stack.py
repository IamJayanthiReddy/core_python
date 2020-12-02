"""
stack follows Last in First out (LIFO) order
"""

class Stack(object):

    def __init__(self):
        self.item = []

    def push(self, item):
        """
        Push the elements to the last index
        :return: None
        """
        self.item.append(item)

    def pop(self):
        """
        This will remove the last element
        :return: None
        """
        self.item.pop()
        pass

    def peek(self):
        """
        Allows to see the last element of the stack
        :return: last element
        """
        if self.item:
            return self.item[-1]
        else:
            return None

    def isempty(self):
        """
        Tells whether the stack is Empty or not
        :return: Boolean value (True - if empty, False - if not empty)
        """
        if self.item == []:
            return True
        else:
            return False

if __name__ == "__main__":
    stack = Stack()
    stack.push('1')
    stack.push('2')
    print(stack.peek())

    stack.pop()
    print(stack.peek())
    print(stack.isempty())