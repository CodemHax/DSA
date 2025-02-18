
def largestOddNumber(num):
        numList = list(num)
        lists = [int(char) for char in numList]
        largest = 0
        print(lists)
        nuber = 0
        for i in lists:
            int(i)
            if i % 2 != 0 and i > largest:
                largest = i
                for j in range(len(numList)):
                    print(i, numList[j])













if __name__ == "__main__":
    num = ("52546434455555555599")
    largestOddNumber(num)