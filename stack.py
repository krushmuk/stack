closing = [']', '}', ')']
bracket_dict = {'[': ']', '{': '}', '(': ')'}
from Stack import stack


def check_balance(string):
    string = list(string)
    br_stack = stack.Stack()
    for bracket in string:
        if bracket in closing:
            if br_stack.size() == 0 or bracket_dict[br_stack.pop()] != bracket:
                return 'Несбалансированно'
        else:
            br_stack.push(bracket)
    if br_stack.size() != 0:
        return 'Несбалансированно'
    return 'Cбалансированно'


print(check_balance('[]{({})}'))
