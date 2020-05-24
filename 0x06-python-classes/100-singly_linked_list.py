#!/usr/bin/python3

"""Single linked list module"""


class Node:
    '''
    Node class of a singly linked list
    Attributes:
        data (int): data of singly linked list
        next_node (int): node of singly linked list
    '''

    def __init__(self, value, next_node=None):
        ''' class constructor '''

        self.data = value
        self.next_node = next_node

    @property
    def data(self):
        '''
        data getter
        Returns:
            data: the stored data
        '''

        return self.__data

    @data.setter
    def data(self, value):
        '''
        data attribute setter
        Args:
            value (int): value to be set in data
        Returns:
            TypeError: if value is not an int
        '''

        if type(value) != int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        '''
        next_node attribute getter
        Returns:
            next_node: pointer to next node
        '''

        return self.__next_node

    @next_node.setter
    def next_node(self, node):
        '''
        next_node attribute setter
        Args:
            node: singly linked list node
        Returns:
            TypeError: next_node can be None or must be a Node,
        '''

        if not isinstance(node, Node) and node is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = node


class SinglyLinkedList(object):
    '''
    Singly linked list class
    Attributes:
        head (Node): pointer to the first node in singly linked list
    '''

    def __init__(self):
        '''Initializer for the SinglyLinkedList class'''

        self.__head = None

    def __str__(self):

        data_holder = ""
        pointer = self.__head

        while pointer:
            data_holder += str(pointer.data)
            if pointer.next_node:
                data_holder += '\n'
            pointer = pointer.next_node

        return data_holder

    def sorted_insert(self, value):

        ''' sort and insert '''

        newnode = Node(value)

        if self.head is None:
            self.head = newnode

        elif self.head.data > newnode.data:
            newnode.next_node = self.head
            self.head = newnode
            return

        temp = self.head
        while temp:
            if temp.next_node is None:
                break
            if newnode.data > self.head.data and \
                    temp.next_node.data > newnode.data:
                newnode.next_node = temp.next_node
                temp.next_node = newnode
                return
            temp = temp.next_node
        temp.next_node = newnode
        newnode.next_node = None
