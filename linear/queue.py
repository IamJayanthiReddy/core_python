"""
Queue follows First in First Out order

Ex: People standing in ATM to withdraw money
"""

class Queue(object):

    def __init__(self):
        self.item = []

    def enqueue(self, item):
        """
        Adding elements to the queue from left to right (at the starting)
        :return: None
        """
        self.item.insert(0,item)

    def dequeue(self):
        """
        Deleting elements from the queue
        :return:
        """
        if self.item:
            self.item.pop()
        else:
            return None

    def peek(self):
        """
        To fetch the last element
        :return: last element
        """
        if self.item:
            return self.item[-1]

    def is_empty(self):
        """
        Tells whether the stack is Empty or not
        :return: Boolean value (True - if empty, False - if not empty)
        """
        if self.item == []:
            return True
        else:
            return False

if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    print(queue.is_empty())
    print("peek element\t{}".format(queue.peek()))
    queue.dequeue()
    print("peek element\t{}".format(queue.peek()))
    queue.dequeue()
    print(queue.is_empty())