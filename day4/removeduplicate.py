def remove_duplicate(arr):
    count = 0
    un = []
    for i in arr:
        if i not in un:
            un.append(i)
            count += 1
    un.sort()
    arr[:] = un
    return len(arr)


class RemoveDuplicate:
    pass


if __name__ == "__main__":
    numbs = [-1,0,0,0,0,3,3]

    obj = remove_duplicate(numbs)
    print(obj)
