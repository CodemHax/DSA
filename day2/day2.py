#
#
# head = { "value" : 5,
#           "Next": { "value" : 7,
#                     "Next": {  "value" : 8,
#                                 "Next": { "value" :9,
#                                            "Next": { "value" : 10,
#                                                       "Next": {}
#
#                                            }
#
#                                 }
#
#                     }
#
#           }
#
# }
#
# print(head["Next"]["Next"]["Next"]["Next"]["value"])

def nStarTriangle(n :int):
    for i in range(n):
        for j in range(n-i-1):
            print(" ", end="")
        for j in range(2*i+1):
            print("*",end="")
        for j in range(n-i-1):
            print(" ", end="")
        print()
nStarTriangle(5)

class Node:
     def __init__(self, value):
         self.value = value
         self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None :
          self.head = new_node
          self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1


my_linked_list = LinkedList(4)
my_linked_list.append(10)
my_linked_list.print_list()

# print('Head:', my_linked_list.head.value)
# print('Tail:', my_linked_list.tail.value)
# print('Length:', my_linked_list.length)
