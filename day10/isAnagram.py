def isAnagram(s, t):
    list_s = list()
    list_t = list()
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        list_s.append(s[i])
        list_t.append(t[i])
    print(list_s, list_t)

    for x , y in (list_s,list_s):
        if y not in list_s:
            return False
        if x not in list_t:
            return False
    return True

def isAnagram(s, t):
    list_s = list(s)
    list_t = list(t)
    if len(s) != len(t):
        return False
    for x in list_s:
        if list_s.count(x) != list_t.count(x):
            return False
    return True


from collections import Counter

def isAnagram(s, t):
    return Counter(s) == Counter(t)

if __name__ == "__main__":
    s = "paper"
    t = "titl"
    print(isAnagram(s, t))