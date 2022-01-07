class Stack:

    def __init__(self):
        self.stack = []

    def push(self, object):
        self.stack.append(object)

def pop(self):
    if len(self.stack) == 0:
        raise 'Error', 'stack is empty'
    obj = self.stack[-1]
    del self.stack[-1]
    return obj

def isempty(self):
    if len(self.stack) == 0:
        return True
    else:
        return False

def top(self):
    return self.stack[-1]

def show(self):
    print self.stack

