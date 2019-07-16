from stack import Stack


class StackQueue(object):
    """Queue implementaion usig 2 stacks."""

    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

class Queue1(StackQueue):
    """ queue using 2 stacks with costly enqueue operation """

    def __init__(self):
        super (queue1, self).__init__()
        self.top = -1
    def enqueue(self, data):
        if not self.s1.isEmpty():
            # push all data from stack1 to stack2
            while not self.s1.isEmpty():
                d = self.s1.pop()
                self.s2.push(d)
        self.s1.push(data)

        #push back all data from stack2 to stack1
        while not self.s2.isEmpty():
            d = self.s2.pop()
            self.s1.push(d)

    def dequeue(self):
        return self.s1.pop()

class Queue2(StackQueue):
    """ queue using 2 stacks with costly dequeue operation """

    def __init__(self):
        pass

    def enqueue(self, data):
        self.s1.push(data)

    def dequeue(self):
        # if stack2 is not empty, pop element
        if not self.s2.isEmpty():
            return self.s2.pop()

        # else push all element from stack1 to stack2
        while not self.s1.isEmpty():
            d = self.s1.pop()
            self.s2(d)
        return self.s2.pop()

if __name__ == '__main__':
    # driver code
    q1 = Queue1()
    q1.enqueue(1)       #[1]
    q1.enqueue(2)       #[1,2]
    q1.enqueue(3)       #[1, 2, 3]
    print(q1.dequeue()) #[2, 3] ===>1
    q1.enqueue(4)       #[2, 3, 4]
    print(q1.dequeue()) #[3, 4]===>2
    print(q1.dequeue()) #[4] ===>3
    print(q1.dequeue()) #[] ===>4
