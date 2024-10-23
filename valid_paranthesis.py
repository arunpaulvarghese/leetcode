# valid paranthesis
def validParanthesis(param):
    dic = {
        "[":"]",
        "{":"}",
        "(":")"
    }
    stack = []
    for bracket in param:
        if bracket in dic:
            stack.append(bracket)
        elif len(stack) == 0 or bracket != dic[stack.pop()]:
            return False
    if len(stack) == 0:
        return True
    else:
        return False



p = "[[{()}]]"
print(validParanthesis(p))

