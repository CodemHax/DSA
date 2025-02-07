from audioop import reverse


def reverseWords(string):
    split = list(filter(None, string.split(" ")))
    print(split)
    reverse = reversed(split)
    reverse_string = " ".join(reverse)
    return reverse_string


if __name__ == "__main__":
    string = "  hello world  "
    print(reverseWords(string))