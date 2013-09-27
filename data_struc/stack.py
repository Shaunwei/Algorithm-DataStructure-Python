#STACK
"""
STACK-EMPTY(S)
1  if top[S] = 0
2      then return TRUE
3      else return FALSE

PUSH(S, x)
1  top[S] ← top[S] + 1
2  S[top[S]] ← x

POP(S)
1  if STACK-EMPTY(S)
2     then error "underflow"
3     else top[S] ← top[S] - 1
4          return S[top[S] + 1]
"""

class Stack(object):
    def __init__(self):
        self.items = []
    
    def push(self,item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
        
    def isEmpty(self):
        return (self.items ==[])