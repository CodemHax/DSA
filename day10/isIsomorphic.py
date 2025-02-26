def isIsomorphic(s , t):
    s_dict = {}
    t_dict = {}
    for i in range(len(s)):
        if s[i] in s_dict:
            if s_dict[s[i]] != t[i]:
                return False
        else:
            s_dict[s[i]] = t[i]

        if t[i] in t_dict:
            if t_dict[t[i]] != s[i]:
                return False
        else:
            t_dict[t[i]] = s[i]
    return True


if __name__ == "__main__":
    s = "paper"
    t = "title"
    print(isIsomorphic(s, t))