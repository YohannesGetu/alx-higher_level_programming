#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.__data = data
        if not isinstance(next_node, Node) and next_node is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and next_node is not None:
            raise TypeError("next_node must be a Node object")
        self.__data = value

class SinglyLinkedList:
    linked_list = []
    def __init__(self):
        pass

    def sorted_insert(self, value):
        new_node = Node(value)
        self.linked_list.append(Node.data)
        sorted_list = self.linked_list.sort()

    def __str__(self):
        for i in self.sorted_list:
            print(i)
