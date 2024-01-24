#!/usr/bin/python3

"""This defines classes for a singly-linked list"""


class Node:
    """This represents a node in a singly-linked list"""

    def __init__(self, data, next_node=None):
        """This initializes a new node

        Args:
            data (int): This is the data of the new node
            next_node (Node): This is the next node of the new node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """This gets/sets the data of the node"""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """This gets/sets the next_node of the node"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """This represents a singly-linked list"""

    def __init__(self):
        """This initalizes a new singly-linked list"""
        self.__head = None

    def sorted_insert(self, value):
        """This inserts a new node to the singly-linked list

        This node is inserted into the list at the correct
        ordered numerical position

        Args:
            value (Node): This is the new node to insert
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """This defines the print() representation of a singly-linked list"""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
