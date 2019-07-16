import logging
logging.info(__name__)

class Stack(object):
    """Python implementaion of Stack using list"""
    def __init__(self):
        self.items = []

    def __str__(self):
        return '->'.join(str(x) for x in self.items)
        
    # __repr__ is same as __str__
    __repr__=__str__

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

class SpecialStack(Stack):
    '''All opration in O(n), getMin'''
    def __init__(self):
        super(SpecialStack, self).__init__()
        self.min_value = None

    def __str__(self):
        return '->'.join(str(x) for x in self.items)

    def push(self, ele):
        if self.isEmpty():
            self.items.append(ele)
            self.min_value = ele
        else:
            if ele >= self.min_value:
                self.items.append(ele)
            else:
                mn = (2*ele) - self.min_value
                self.min_value = ele
                self.items.append(mn)

    def pop(self):
        ele = self.items.pop()
        if ele >= self.min_value:
            return ele
        else:
            mn = self.min_value
            self.min_value = (2*mn) - ele
            return mn

    def getMin(self):
        if self.isEmpty():
            print('stack is empty')
        else:
            return self.min_value

if __name__ == '__main__':
    s = SpecialStack()
    s.push(14)
    s.push(11)
    s.push(15)
    s.push(10)
    s.push(34)
    print(str(s))
    print('minimum : %s'%s.getMin())
    print(s.pop())
    s.push(9)
    print('minimum : %s'%s.getMin())
    print(str(s))
    print(s.pop())
    print('minimum : %s'%s.getMin())
    print(str(s))
    print(s.pop())
    print('minimum : %s'%s.getMin())
    print(str(s))
    print(s.pop())
    print('minimum : %s'%s.getMin())
    print(str(s))
    print(s.pop())
    print('minimum : %s'%s.getMin())
    print(str(s))
