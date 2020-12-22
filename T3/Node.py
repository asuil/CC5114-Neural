"""
author: Ariel Suil Aravena [asuil]
date: 21-12-2020 (last modified on: 21-12-2020)

Library to manipulate Program Trees on Tarea 3

Node:
    Add:    adds two nodes
    Mult:   multiplies two nodes
    Div:    divides two nodes (secure x/0=1)
    Sub:    substracts two nodes

Leaf:
    Number:     constant number
    Variable:   variable number (input on evaluate)

toString:   converts node/leaf to string for printing
evaluate:   resolves ecuation using variables from 'args' dict
copy:       creates a copy of the node and its children
replace:    replaces a child on a node using the given binIndex and newNode
                - binIndex is a string representation of a binary number (bin(x)[2:])
                - newNode is the node to replace with on the child
subcopy:    copies tree from a specific node onwards, binIndex determines node
"""


class Node:

    # function to fill on implementations, string version of function
    nodeFunction = lambda x, y: 0
    nodeString = "empty node"

    def __init__(self, left, right):
        self.__l = left
        self.__r = right

    def toString(self):
        return f"({self.__l.toString()} {type(self).nodeString} {self.__r.toString()})"

    def evaluate(self, args):
        return type(self).nodeFunction(self.__l.evaluate(args), self.__r.evaluate(args))

    def copy(self):
        return type(self)(self.__l.copy(), self.__r.copy())

    def replace(self, binIndex, newNode):
        # on last Node
        if len(binIndex) == 1:
            if int(binIndex):
                self.__r = newNode.copy()
            else:
                self.__l = newNode.copy()
            # replace successfull
            return True

        if int(binIndex[0]):
            replaced = self.__r.replace(binIndex[1:], newNode)
        else:
            replaced = self.__l.replace(binIndex[1:], newNode)

        # case leaf reached
        if not replaced:

            # replace here
            if int(binIndex[0]):
                self.__r = newNode.copy()
            else:
                self.__l = newNode.copy()

        return True

    def subcopy(self, binIndex):

        # on last Node
        if len(binIndex) == 1:
            if int(binIndex):
                return self.__r.copy()
            else:
                return self.__l.copy()

        if int(binIndex[0]):
            return self.__r.subcopy(binIndex[1:])
        else:
            return self.__l.subcopy(binIndex[1:])


class Add(Node):

    nodeFunction = lambda x, y: x + y
    nodeString = "+"


class Mult(Node):

    nodeFunction = lambda x, y: x * y
    nodeString = "*"


class Sub(Node):

    nodeFunction = lambda x, y: x - y
    nodeString = "-"


class Div(Node):

    nodeFunction = lambda x, y: x / y if y != 0 else 1
    nodeString = "%"


class Leaf:

    leafFunction = lambda x, args: 0

    def __init__(self, value):
        self.__v = value

    def toString(self):
        return str(self.__v)

    def evaluate(self, args):
        return type(self).leafFunction(self.__v, args)

    def copy(self):
        return type(self)(self.__v)

    def replace(self, binIndex, newNode):
        return False

    def subcopy(self, binIndex):
        return self.copy()

class Number(Leaf):

    leafFunction = lambda x, args: x


class Variable(Leaf):

    leafFunction = lambda x, args: args[x]


if __name__ == '__main__':

    node = Add(
        Number(4),
        Mult(
            Variable("x"),
            Div(
                Number(5),
                Sub(
                    Number(5),
                    Variable("y")
                )
            )
        )
    )

    nodeCopy = node.copy()
    node2 = Sub(Number(4), Number(8))

    # simple testing
    print(node.toString())
    node.replace(bin(1)[2:], nodeCopy)
    print(node.toString())
    nodeCopy.replace(bin(5)[2:], node2)
    print(node.toString())
    node2.replace(bin(70)[2:], node)
    print(node2.toString())
    print(node2.evaluate({"x": 5, "y": 1}))
