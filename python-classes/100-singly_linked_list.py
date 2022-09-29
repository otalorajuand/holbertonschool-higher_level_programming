#!/usr/bin/python3
"""Node class"""


class Node:

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """data getter"""
        return (self.__data)

    @data.setter
    def data(self, value):
        """data setter"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """next_node getter"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """data setter"""
        if not isinstance(value, Node) and value:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


"""SinglyLinkedList class"""


class SinglyLinkedList:

    def __init__(self):
        self.__head = None

    def __str__(self):
        current_node = self.__head
        result_string = ""
        while current_node:
            result_string += f'{current_node.data}\n'
            current_node = current_node.next_node
        return (result_string)

    def sorted_insert(self, value):
        current_node = self.__head
        new_node = Node(value)

        if not current_node:
            self.__head = Node(value)
            return

        if current_node.data > value:
            new_node.next_node = current_node
            self.__head = new_node
            return

        while True:
            if not current_node.next_node:
                current_node.next_node = new_node
                break
            if current_node.data < value and
            current_node.next_node.data >= value:
                current_node.next_node = Node(value, current_node.next_node)
                break
            current_node = current_node.next_node
