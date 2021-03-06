#!python3
import math

from sorting_iterative import insertion_sort
from kdtreenode import KDTreeNode


class KDTree(object):
    """
    """

    def __init__(self, dimensions, points=None):
        """Initialize this KD tree and insert the given points, if any."""
        self.root = None
        # Count the number of strings inserted into the tree
        self.size = 0
        # Keep track of how many dimensions the tree represents
        self.dimensions = dimensions
        # Insert each string, if any were given
        if points is not None:
            for point in points:
                self.insert(point)

    def __repr__(self):
        """Return a string representation of this KD tree."""
        return 'KDTree({} nodes)'.format(self.size)

    def is_empty(self):
        """Return True if this KDTree tree is empty (contains no points)."""
        # TODO
        if self.root == None:
            return True
        return False

    def contains(self, point):
        """Return True if this KD tree contains the given point."""
        # TODO
        # Find a node with the given item, if any
        node = self._find_node(point, self.root)
        # Return True if a node was found, or False
        return node is not None

    def find_parent(self, point, node, parent=None):
                # Check if starting node exists
        if node is None:
            # Not found (base case)
            return parent

        # adjust item to compare correct dimension
        axis_index = node.height()%self.dimensions

        # TODO: Check if the given item matches the node's data
        if point[axis_index] == node.data[axis_index]:
            # Return the parent of the found node
            return parent
        # TODO: Check if the given item is less than the node's data
        elif point[axis_index] < node.data[axis_index]:
            # TODO: Recursively descend to the node's left child, if it exists
            return self.find_parent(point, node.left, node)  # Hint: Remember to update the parent parameter
        # TODO: Check if the given item is greater than the node's data
        elif point[axis_index] > node.data[axis_index]:
            # TODO: Recursively descend to the node's right child, if it exists

            return self.find_parent(point, node.right, node)  # Hint: Remember to update the parent parameter

    def insert(self, point):
        """Insert the given point into this KD tree."""
        # TODO
        if self.is_empty():
            # TODO: Create a new root node
            self.root = KDTreeNode(point)
            # TODO: Increase the tree size
            self.size += 1
            return

        else:
            parent = self.find_parent(point, self.root)

            # adjust item to compare correct dimension
            axis_index = parent.height() % self.dimensions

            # Add Node to right side of parent node
            if point[axis_index] < parent.data[axis_index]:
                # TODO: Create a new node and set the parent's left child
                parent.left = KDTreeNode(point)
            # TODO: Check if the given item should be inserted right of parent node
            elif point[axis_index] > parent.data[axis_index]:
                # TODO: Create a new node and set the parent's right child
                parent.right = KDTreeNode(point)
            # TODO: Increase the tree size
            self.size += 1

    def _find_node(self, point, node):
        """
        Check to see if a given point is contained in the tree, returns None if not found
        """
        # Check if starting node exists
        if node is None:
            # Not found (base case)
            return None
        # TODO: Check if the given item matches the node's data
        elif node.data == point:
            # Return the found node
            return node
        # TODO: Check if the given item is less than the node's data
        elif point < node.data:
            # TODO: Recursively descend to the node's left child, if it exists
            return self._find_node(point, node.left)
        # TODO: Check if the given item is greater than the node's data
        elif point > node.data:
            # TODO: Recursively descend to the node's right child, if it exists
            return self._find_node(point, node.right)

    def delete(self, point):
        """Deletes given point from tree"""
        pass


    def _traverse(self, node, visit):
        """Traverse this prefix tree with recursive depth-first traversal.
        Start at the given node with the given prefix representing its path in
        this prefix tree and visit each node with the given visit function."""
        # TODO
        if node is None:
            return
        # TODO: Traverse left subtree, if it exists
        if node.left != None:
            self._traverse(node.left, visit)
        # TODO: Visit this node's data with given function
        visit(node.data)
        # TODO: Traverse right subtree, if it exists
        if node.right != None:
            self._traverse(node.right, visit)

    def distance(self, p1, p2):
        return math.sqrt(sum([((p2[i]-p1[i])**2) for i in range(len(p1))]))


    def nearest_neighbors(self, point, node=None, closest_points=None):
        """
        returns list of all points contained in tree sorted by increasing distance to the point given
        """
        if node is None:
            node = self.root

        if closest_points is None:
            closest_points = list()

        closest_points.append((node.data, self.distance(node.data, point)))

        closest_points.sort(key=lambda x: x[1])

        # add pruning
        if node.left is not None:
            return self.nearest_neighbors(point, node.left, closest_points)
        if node.right is not None:
            return self.nearest_neighbors(point, node.right, closest_points)

        return closest_points


# def create_prefix_tree(strings):
#     print(f'strings: {strings}')
#
#     tree = KDTree()
#     print(f'\ntree: {tree}')
#     print(f'root: {tree.root}')
#     print(f'strings: {tree.strings()}')
#
#     print('\nInserting strings:')
#     for string in strings:
#         tree.insert(string)
#         print(f'insert({string!r}), size: {tree.size}')
#
#     print(f'\ntree: {tree}')
#     print(f'root: {tree.root}')
#
#     print('\nSearching for strings in tree:')
#     for string in sorted(set(strings)):
#         result = tree.contains(string)
#         print(f'contains({string!r}): {result}')
#
#     print('\nSearching for strings not in tree:')
#     prefixes = sorted(set(string[:len(string)//2] for string in strings))
#     for prefix in prefixes:
#         if len(prefix) == 0 or prefix in strings:
#             continue
#         result = tree.contains(prefix)
#         print(f'contains({prefix!r}): {result}')
#
#     print('\nCompleting prefixes in tree:')
#     for prefix in prefixes:
#         completions = tree.complete(prefix)
#         print(f'complete({prefix!r}): {completions}')
#
#     print('\nRetrieving all strings:')
#     retrieved_strings = tree.strings()
#     print(f'strings: {retrieved_strings}')
#     matches = set(retrieved_strings) == set(strings)
#     print(f'matches? {matches}')


def main():

    tree = KDTree(5, [(1,2,3,4,5), (0,1,4,1,2), (2,4,3,6,7), (9,8,10,7,3), (-1,0,0,14,15)])
    tree2 = KDTree(2, [(1,1), (2,2), (3,3), (4,4), (5,5)])
    # print(tree.distance((1,1),(1,1)))
    # print(tree.distance((1,1),(2,2)))
    # print(tree.nearest_neighbors((1,2,3,4,5)))
    # print(tree.nearest_neighbors((0,1,4,1,2)))
    # print(tree.nearest_neighbors((2,4,3,6,7)))
    # print(tree.nearest_neighbors((0,1,3,1,2)))
    #
    # print(tree2.nearest_neighbors((2,2)))
    tree = KDTree(2,[(1,1), (2,2), (4,4)])
    print(tree.nearest_neighbors((1,1)))

#     assert tree.root.data == (1,2,3,4,5)
#     assert tree.root.left.data == (0,1,4,1,2)
#     assert tree.root.right.data == (2,4,3,6,7)
#     assert tree.root.right.right.data == (9,8,10,7,3)
#     assert tree.root.left.left.data == (-1,0,0,14,15)
#     assert tree.size == 5
#     assert tree.is_empty() is False
#     temp = list()
#     print(tree._traverse(tree.root, temp.append))
#     print(temp)
#     print(f'\ntree: {tree}')
#     print(tree.contains((1,2,3,4,5)))
#     print(tree.contains((1,2,11,4,5)))

    # tree = KDTree(3, [(1,2,3), (0,1,4), (2,4,3)])
    # assert tree.root.data == (1,2,3)
    # assert tree.root.left.data == (0,1,4)
    # assert tree.root.right.data == (2,4,3)
    # assert tree.size == 3
    # assert tree.is_empty() is False
    # print(f'\ntree: {tree}')

    # tree = KDTree(2, [(1,1), (3,3), (2,2)])
    # print(f'\ntree: {tree}')
    # assert tree.root.data == (1,1)
    # assert tree.root.left == None
    # assert tree.root.right.data == (3,3)
    # assert tree.root.right.left.data == (2,2)
    # assert tree.size == 3
    # assert tree.is_empty() is False

    # tree = KDTree(1)
    # assert tree.size == 0
    # tree.insert('B')
    # assert tree.size == 1
    # print(f'\ntree: {tree}')
    # tree.insert('A')
    # assert tree.size == 2
    # print(f'\ntree: {tree}')
    # tree.insert('C')
    # assert tree.size == 3
    # print(f'\ntree: {tree}')
#     # Simpe test case of string with partial substring overlaps
#     strings = ['ABC', 'ABD', 'A', 'XYZ']
#     create_prefix_tree(strings)
#
#     # Create a dictionary of tongue-twisters with similar words to test with
#     tongue_twisters = {
#         'Seashells': 'Shelly sells seashells by the sea shore'.split(),
#         # 'Peppers': 'Peter Piper picked a peck of pickled peppers'.split(),
#         # 'Woodchuck': ('How much wood would a wood chuck chuck'
#         #                ' if a wood chuck could chuck wood').split()
#     }
#     # Create a prefix tree with the similar words in each tongue-twister
#     for name, strings in tongue_twisters.items():
#         print(f'{name} tongue-twister:')
#         create_prefix_tree(strings)
#         if len(tongue_twisters) > 1:
#             print('\n' + '='*80 + '\n')


if __name__ == '__main__':
    main()
