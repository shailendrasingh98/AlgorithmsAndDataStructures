#Infix to postfix conversion algorithm
from stack import Stack

class InfixToPostfix(object):
    _operator_precedence = {"^": 3,
                  "*":2,
                  "/":2,
                  "+":1,
                  "-":1,}
    def __init__(self,):
        self._stack = Stack()
        self._postfix =[]

    def isOpretor(self, ch):
        if ch in self._operator_precedence:
            return True
        return False

    def convert(self, expression):
        for ch in expression:
            if ch =='(':
                self._stack.push(ch)
            elif self.isOpretor(ch):
                if self._stack.isEmpty():
                    self._stack.push(ch)
                    #check precedence with top of _stack
                elif self._operator_precedence[ch] <  self._operator_precedence.get(self._stack.peek(), -1):
                    #take out all operator of less precedence
                    while not self._stack.isEmpty() and self.isOpretor(self._stack.peek()):
                        top = self._stack.pop()
                        if self._operator_precedence[ch] < self._operator_precedence[top]:
                            self._postfix.append(top)
                    self._stack.push(ch)
                else:#precedence of incoming char is greater
                    #take out the operator from top of _stack and push in coming char
                    self._postfix.append(self._stack.pop())
                    self._stack.push(ch)

            elif ch == ')':
                while self._stack.peek() != "(":
                    top = self._stack.pop()
                    self._postfix.append(top)
            else:
                self._postfix.append(ch)

        while not self._stack.isEmpty():
            self._postfix.append(self._stack.pop())
        return self._postfix

    def show(self):
        if self._postfix:
            print(self._postfix)

if __name__ == '__main__':
    exp = "A*B+C"
    itop = InfixToPostfix()
    itop.convert(exp)
    itop.show()
