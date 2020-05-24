#!/usr/bin/bash

'''Sorted Sinlgy list'''


class Node:
    '''
    class for Nodes 

        Attributes:
        data(int) : private to store data
        next(node): pointer to the next node 
        '''

        def __init__(self, data, next_node=None):
        ''' Class Constructor '''
 
        self.data = data
        self.next_node = next_node

        @property
        def data(self):

            '''
            data getter

            Returns: the entred data

            '''
            return self.__data

        @data.setter
        def data(self, value):
            '''
            data attribute setter

            Arguments:
                vavlue(int) : value of the data to store in the node

            Return:
                TyperError : if value is set no correctly

            '''

            if type(value) is not int:
                raise typeError("data must be an integer")
            else:
                self.__data = value

        @property
        def next_node(self):
            '''

            getter of next_node attribue

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

            '''print list '''

            listx = []
            pointer = self.head

            while pointer:
                listx.append(str(pointer.data))
                pointer = pointer.next

        return '\n'.join(listx)    
    
  
        def sorted_insert(self, data):
            '''
            insert sorted data
            '''

            newnode = Node(value)

            if self.__head is None:
                self.___head = newnode

            elif self.head.data > newnode.data:
                newnode.next_node = self.head
            self.__head = newnode
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
