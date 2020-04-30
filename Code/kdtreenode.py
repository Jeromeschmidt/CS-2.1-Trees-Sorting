#!python3


class KDTreeNode:
    """KDTreeNode: A node for use in a prefix tree that stores a single
    character from a string and a structure of children nodes below it, which
    associates the next character in a string to the next node along its path from
    the tree's root node to a terminal node that marks the end of the string."""

    # Choose an appropriate type of data structure to store children nodes in
    # Hint: Choosing list or dict affects implementation of all child methods
    CHILDREN_TYPE = dict # or list

    def __init__(self, data):
        """Initialize this prefix tree node with the given character value, an
        empty structure of children nodes, and a boolean terminal property."""
        # Data that this node represents
        self.data = data
        # left and right child nodes
        self.left = None
        self.right = None
        # Marks what dimension this node represents
        self.dimension = None

    def get_dimension(self):
        """Return dimension that this node represents."""
        return self.dimension

    def num_children(self):
        """Return the number of children nodes this prefix tree node has."""
        # TODO: Determine how many children this node has
        return len(self.children.keys())

    def is_leaf(self):
        """Return True if this node is a leaf (has no children)."""
        # TODO: Check if both left child and right child have no value
        return (self.left == None) and (self.right == None)

    def is_branch(self):
        """Return True if this node is a branch (has at least one child)."""
        # TODO: Check if either left child or right child has a value
        return (self.left != None) or (self.right != None)

    def add_child(self):
        ## TODO:
        pass

    def height(self):
        """Return the height of this node (the number of edges on the longest
        downward path from this node to a descendant leaf node).
        TODO: Best and worst case running time: O(n) under all conditions"""
        # TODO: Check if left child has a value and if so calculate its height
        if self is None:
            return 0
        else:
            # return max(self.left.height(), self.right.height()) + 1
            height_1 = 0
            height_2 = 0
            if self.left != None:
                height_1 = self.left.height() + 1
            # TODO: Check if right child has a value and if so calculate its height
            if self.right != None:
                height_2 = self.right.height() + 1
            # Return one more than the greater of the left height and right height
            if height_1 > height_2:
                return height_1
            return height_2

    def __repr__(self):
        """Return a code representation of this prefix tree node."""
        return f'KDTreeNode({self.character!r})'

    def __str__(self):
        """Return a string view of this prefix tree node."""
        return f'({self.character})'
