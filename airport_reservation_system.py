#!python3
import math


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key
        self.size_node = 1


class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def increment_rank(self, node, key):
        if node:
            if node.key == key:
                if node.left:
                    return 1+node.left.size_node
                return 1
            if node.key > key:
                return self.increment_rank(node.left, key)
            else:
                return self.increment_rank(node.right, key)+node.left.size_node+1

    def rank(self, key):
        return self.increment_rank(self.root, key)

    def increment_size_node(self, node, key):
        if node:
            if node.key == key:
                return
            node.size_node += 1
            if node.key > key:
                self.increment_size_node(node.left, key)
            else:
                self.increment_size_node(node.right, key)

    def increment_size_nodes(self, key):
        if self.root == key:
            self.root.size_node += 1
        else:
            self.increment_size_node(self.root, key)

    def insert_node(self, node, key, k):
        if abs(node.key-key) >= k:
            if node.key > key:
                if node.left is None:
                    node.left = Node(key)
                else:
                    if not self.insert_node(node.left, key, k):
                        return False
            else:
                if node.right is None:
                    node.right = Node(key)
                else:
                    if not self.insert_node(node.right, key, k):
                        return False
        else:
            return False
        return True

    def insert(self, key, k):
        if self.root:
            if not self.insert_node(self.root, key, k):
                return False
        else:
            self.root = Node(key)
        self.size += 1
        return True


if __name__ == "__main__":
    tree = BinaryTree()
    k = int(input())
    reservations = list(map(int, input().split()))
    t = int(input())
    for time in reservations:
        if tree.insert(time, k):
            tree.increment_size_nodes(time)
    print('The number of flights scheduled before and at time entered : {}'.format(
        tree.rank(t)))
