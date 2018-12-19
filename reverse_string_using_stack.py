from stack import Stack
"""Reverse a string using stack
   Time Complexity  = O(n)
   Space Complexity = O(n)
"""
def reverse_string(strg, stack = None):
    stack = stack or Stack()
    for char in strg:
        stack.push(char)
    strg = [stack.pop() for i in range(len(strg))]
    return ''.join(strg)

def main():
    s = Stack()
    print(reverse_string('aagimnf',s))
