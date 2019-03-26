"""问题地址： https://leetcode.com/problems/add-two-numbers/"""

import extend.extend as extend


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


@extend.exe_time
def add_two_numbers(linked_list1, linked_list2):
    node1 = linked_list1.head
    node2 = linked_list2.head
    result_linked_list = LinkedList()
    p = 0
    while node1 or node2:
        if node1 is not None and node2 is not None:
            temp = node1.data + node2.data + p
        elif node1 is None and node2 is not None:
            temp = node2.data + p
        elif node1 is not None and node2 is None:
            temp = node1.data + p
        else:
            temp = 0

        p = 0
        if temp > 9:
            temp = temp % 10
            p = 1
        result_linked_list.append(temp)
        if node1 is not None:
            node1 = node1.next
        if node2 is not None:
            node2 = node2.next
    if p != 0:
        result_linked_list.append(p)
    result_linked_list.print_list()
    return result_linked_list


def main():
    # first LinkedList
    linked_list1 = LinkedList()
    for i in range(9):
        linked_list1.append(i)
    linked_list1.print_list()

    # second LinkedList
    linked_list2 = LinkedList()
    for i in range(10):
        linked_list2.append(i)
    linked_list2.print_list()

    add_two_numbers(linked_list1, linked_list2)


main()
