
def compare_first_to_next(lst):
    for i in range(len(lst) - 1):
        if lst[i] == lst[i + 1]:
            print(f"Element {lst[i]} at index {i} is equal to element {lst[i + 1]} at index {i + 1}")
        else:
            print(f"Element {lst[i]} at index {i} is not equal to element {lst[i + 1]} at index {i + 1}")

# Example usage
lst = "(()())(())"
list = list(lst)
compare_first_to_next(lst)