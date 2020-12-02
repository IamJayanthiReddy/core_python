"""
Program to chech whether paranthesis is balanced or not using Stack
"""

from data_structures.linear.stack import *

def match_symbol(symbol_str):
    symbol_pairs = {
        '(':')',
        '[':']',
        '{':'}'
    }

    openers = symbol_pairs.keys()
    mystack = Stack()

    index = 0
    while(index < len(symbol_str)):
        symbol = symbol_str[index]
        if symbol in openers:
            mystack.push(symbol)
        else:
            if mystack.isempty():
                return False
            else:
                top_item = mystack.pop()
                if symbol != symbol_pairs[top_item]:
                    return False
        index+=1
    if mystack.isempty():
        return True

    return False
match_symbol("([{}]))")
match_symbol("(([{]})))")

