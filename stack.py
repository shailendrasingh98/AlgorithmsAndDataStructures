import logging
logging.info(__name__)

class Stack():
    """Python implementaion of Stack using list"""
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        logging.info('Adding {0} to Stack'.format(item))
        self.items.append(item)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError as e:
            logging.info('Stack is empty')
            return None

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
