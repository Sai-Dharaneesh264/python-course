from stack import Stack


def is_match(left, right):
    if (left == '(' and right == ')'):

        return True
    elif (left == '[' and right == ']'):
        return True
    elif (left == '{' and right == '}'):
        return True
    else:
        print("false from here")
        return False

def is_paren_balanced(paren_string):
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(paren_string):
        paren = paren_string[index]
        if paren in "({[":
            s.push(paren)
        else:
            if s.is_empty():
                return False
            else:
                top = s.pop()
                if not is_match(top, paren):
                    return False
        index += 1
    
    return s.is_empty()

print("String : (((({})))) Balanced or not?")
print(is_paren_balanced("(((({}))))"))

print("String : [][]]] Balanced or not?")
print(is_paren_balanced("[][]]]"))

print("String : [][] Balanced or not?")
print(is_paren_balanced("[][]"))

print("String : ]] Balanced or not?")
print(is_paren_balanced("]]]]"))



