def rotateString(s: str, goal: str):
    if len(s) != len(goal):
        return False
    main = s + s
    if goal in main:
        return True
    else:
        return False


if __name__== "__main__":
    s = "aa"
    goal = "a"
    print(rotateString(s, goal))
