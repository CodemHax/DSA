def removeOuterParentheses(s):
    stack = []
    balanced = 0
    m  = 0
    for i in s :
        if i =='(' :
            m += 1
            if balanced > 0:
              stack.append(i)
            balanced += 1

            print(f"balanced on {m}", balanced)
        elif i ==')' :
             m += 1
             balanced -= 1
             if balanced > 0:
               stack.append(i)
             print(f"balanced on {m}", balanced)
    talk = " ".join(stack)
    return str(talk).replace(" ", "")


class Solution(object):
    pass
if __name__== "__main__":
    s = "(()())(())"
    print(removeOuterParentheses(s))