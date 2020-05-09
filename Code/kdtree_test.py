#!python

from kdtree import KDTree, KDTreeNode
import unittest


class KDTreeNodeTest(unittest.TestCase):

    def test_init(self):
        data = 123
        node = KDTreeNode(data)
        assert node.data is data
        assert node.left is None
        assert node.right is None

    def test_is_leaf(self):
        # Create node with no children
        node = KDTreeNode(2)
        assert node.is_leaf() is True
        # Attach left child node
        node.left = KDTreeNode(1)
        assert node.is_leaf() is False
        # Attach right child node
        node.right = KDTreeNode(3)
        assert node.is_leaf() is False
        # Detach left child node
        node.left = None
        assert node.is_leaf() is False
        # Detach right child node
        node.right = None
        assert node.is_leaf() is True

    def test_is_branch(self):
        # Create node with no children
        node = KDTreeNode(2)
        assert node.is_branch() is False
        # Attach left child node
        node.left = KDTreeNode(1)
        assert node.is_branch() is True
        # Attach right child node
        node.right = KDTreeNode(3)
        assert node.is_branch() is True
        # Detach left child node
        node.left = None
        assert node.is_branch() is True
        # Detach right child node
        node.right = None
        assert node.is_branch() is False

    def test_height(self):
        # Create node with no children
        node = KDTreeNode(4)
        assert node.height() == 0
        # Attach left child node
        node.left = KDTreeNode(2)
        assert node.height() == 1
        # Attach right child node
        node.right = KDTreeNode(6)
        assert node.height() == 1
        # Attach left-left grandchild node
        node.left.left = KDTreeNode(1)
        assert node.height() == 2
        # Attach right-right grandchild node
        node.right.right = KDTreeNode(8)
        assert node.height() == 2
        # Attach right-right-left great-grandchild node
        node.right.right.left = KDTreeNode(7)
        assert node.height() == 3


class KDTreeTest(unittest.TestCase):

    def test_init(self):
        tree = KDTree(1)
        assert tree.root is None
        assert tree.size == 0
        assert tree.is_empty() is True

    def test_init_with_list_dim_2(self):
        tree = KDTree(2, [(1,1), (3,3), (2,2)])
        assert tree.root.data == (1,1)
        assert tree.root.left == None
        assert tree.root.right.data == (3,3)
        assert tree.root.right.left.data == (2,2)
        assert tree.size == 3
        assert tree.is_empty() is False

    def test_init_with_list_dim_3(self):
        tree = KDTree(3, [(1,2,3), (0,1,4), (2,4,3)])
        assert tree.root.data == (1,2,3)
        assert tree.root.left.data == (0,1,4)
        assert tree.root.right.data == (2,4,3)
        assert tree.size == 3
        assert tree.is_empty() is False

    def test_init_with_larger_list_dim_5(self):
        tree = KDTree(5, [(1,2,3,4,5), (0,1,4,1,2), (2,4,3,6,7), (9,8,10,7,3), (-1,0,0,14,15)])
        assert tree.root.data == (1,2,3,4,5)
        assert tree.root.left.data == (0,1,4,1,2)
        assert tree.root.right.data == (2,4,3,6,7)
        assert tree.root.right.right.data == (9,8,10,7,3)
        assert tree.root.left.left.data == (-1,0,0,14,15)
        assert tree.size == 5
        assert tree.is_empty() is False

    def test_size(self):
        tree = KDTree(1)
        assert tree.size == 0
        tree.insert('B')
        assert tree.size == 1
        tree.insert('A')
        assert tree.size == 2
        tree.insert('C')
        assert tree.size == 3

    def test_nearest_neighbors(self):
        tree = KDTree(2,[(1,1), (2,2), (4,4)])
        neighbors = tree.nearest_neighbors((0,0))
        assert neighbors[0] == ((1, 1), 1.4142135623730951)
        assert neighbors[1] == ((2, 2), 2.8284271247461903)
        assert neighbors[2] == ((4, 4), 5.656854249492381)

        neighbors2 = tree.nearest_neighbors((1,1))
        assert neighbors2[0] == ((1, 1), 0)
        assert neighbors2[1] == ((2, 2), 1.4142135623730951)
        assert neighbors2[2] == ((4, 4), 4.242640687119285)

    #
    # def test_search_with_3_items(self):
    #     # Create a complete binary search tree of 3 items in level-order
    #     items = [2, 1, 3]
    #     tree = KDTree(items)
    #     assert tree.search(1) == 1
    #     assert tree.search(2) == 2
    #     assert tree.search(3) == 3
    #     assert tree.search(4) is None
    #
    # def test_search_with_7_items(self):
    #     # Create a complete binary search tree of 7 items in level-order
    #     items = [4, 2, 6, 1, 3, 5, 7]
    #     tree = KDTree(items)
    #     for item in items:
    #         assert tree.search(item) == item
    #     assert tree.search(8) is None
    #
    # def test_search_with_3_strings(self):
    #     # Create a complete binary search tree of 3 items in level-order
    #     items = ['B', 'A', 'C']
    #     tree = KDTree(items)
    #     assert tree.search('A') == 'A'
    #     assert tree.search('B') == 'B'
    #     assert tree.search('C') == 'C'
    #     assert tree.search('D') is None
    #
    # def test_search_with_7_strings(self):
    #     # Create a complete binary search tree of 7 items in level-order
    #     items = ['D', 'B', 'F', 'A', 'C', 'E', 'G']
    #     tree = KDTree(items)
    #     for item in items:
    #         assert tree.search(item) == item
    #     assert tree.search('H') is None
    #
    # def test_insert_with_3_items(self):
    #     # Create a complete binary search tree of 3 items in level-order
    #     tree = KDTree()
    #     tree.insert(2)
    #     assert tree.root.data == 2
    #     assert tree.root.left is None
    #     assert tree.root.right is None
    #     tree.insert(1)
    #     assert tree.root.data == 2
    #     assert tree.root.left.data == 1
    #     assert tree.root.right is None
    #     tree.insert(3)
    #     assert tree.root.data == 2
    #     assert tree.root.left.data == 1
    #     assert tree.root.right.data == 3
    #
    # def test_insert_with_7_items(self):
    #     # Create a complete binary search tree of 7 items in level-order
    #     items = [4, 2, 6, 1, 3, 5, 7]
    #     tree = KDTree()
    #     for item in items:
    #         tree.insert(item)
    #     assert tree.root.data == 4
    #     assert tree.root.left.data == 2
    #     assert tree.root.right.data == 6
    #     assert tree.root.left.left.data == 1
    #     assert tree.root.left.right.data == 3
    #     assert tree.root.right.left.data == 5
    #     assert tree.root.right.right.data == 7
    #
    # def test_delete_with_3_items(self):
    #     # Create a complete binary search tree of 3 items in level-order
    #     items = [2, 1, 3]
    #     # items = [2, 1]
    #     tree = KDTree(items)
    #     assert tree.root.data == 2
    #     assert tree.root.left.data == 1
    #     assert tree.root.right.data == 3
    #     # # TODO: Test structure of tree after each deletion
    #     tree.delete(2)
    #     assert tree.root.data == 3
    #     assert tree.root.left.data is 1
    #     assert tree.root.right is None
    #     tree.delete(1)
    #     assert tree.root.data == 3
    #     assert tree.root.left is None
    #     assert tree.root.right is None
    #     tree.delete(3)
    #     assert tree.root is None
    #     # assert tree.root.left is None
    #     # assert tree.root.right is None
    #
    # def test_delete_with_7_items(self):
    #     # Create a complete binary search tree of 7 items in level-order
    #     items = [4, 2, 6, 1, 3, 5, 7]
    #     tree = KDTree(items)
    #     # TODO: Test structure of tree after each deletion
    #     tree.delete(4)
    #     assert tree.root.data == 5
    #     assert tree.root.left.data == 2
    #     assert tree.root.right.data == 6
    #     assert tree.root.left.left.data == 1
    #     assert tree.root.right.right.data == 7
    #     tree.delete(6)
    #     assert tree.root.data == 5
    #     assert tree.root.left.data == 2
    #     assert tree.root.right.data == 7
    #     assert tree.root.left.left.data == 1
    #     assert tree.root.right.right == None
    #     tree.delete(2)
    #     assert tree.root.data == 5
    #     assert tree.root.left.data == 3
    #     assert tree.root.right.data == 7
    #     assert tree.root.left.left.data == 1
    #     assert tree.root.right.right == None
    #
    # def test_items_in_order_with_3_strings(self):
    #     # Create a complete binary search tree of 3 strings in level-order
    #     items = ['B', 'A', 'C']
    #     tree = KDTree(items)
    #     # Ensure the in-order traversal of tree items is ordered correctly
    #     assert tree.items_in_order() == ['A', 'B', 'C']
    #
    # def test_items_pre_order_with_3_strings(self):
    #     # Create a complete binary search tree of 3 strings in level-order
    #     items = ['B', 'A', 'C']
    #     tree = KDTree(items)
    #     # Ensure the pre-order traversal of tree items is ordered correctly
    #     assert tree.items_pre_order() == ['B', 'A', 'C']
    #
    # def test_items_post_order_with_3_strings(self):
    #     # Create a complete binary search tree of 3 strings in level-order
    #     items = ['B', 'A', 'C']
    #     tree = KDTree(items)
    #     # Ensure the post-order traversal of tree items is ordered correctly
    #     assert tree.items_post_order() == ['A', 'C', 'B']
    #
    # def test_items_level_order_with_3_strings(self):
    #     # Create a complete binary search tree of 3 strings in level-order
    #     items = ['B', 'A', 'C']
    #     tree = KDTree(items)
    #     # Ensure the level-order traversal of tree items is ordered correctly
    #     assert tree.items_level_order() == ['B', 'A', 'C']
    #
    # def test_items_in_order_with_7_numbers(self):
    #     # Create a complete binary search tree of 7 items in level-order
    #     items = [4, 2, 6, 1, 3, 5, 7]
    #     tree = KDTree(items)
    #     # Ensure the in-order traversal of tree items is ordered correctly
    #     assert tree.items_in_order() == [1, 2, 3, 4, 5, 6, 7]
    #
    # def test_items_pre_order_with_7_numbers(self):
    #     # Create a complete binary search tree of 7 items in level-order
    #     items = [4, 2, 6, 1, 3, 5, 7]
    #     tree = KDTree(items)
    #     # Ensure the pre-order traversal of tree items is ordered correctly
    #     assert tree.items_pre_order() == [4, 2, 1, 3, 6, 5, 7]
    #
    # def test_items_post_order_with_7_numbers(self):
    #     # Create a complete binary search tree of 7 items in level-order
    #     items = [4, 2, 6, 1, 3, 5, 7]
    #     tree = KDTree(items)
    #     # Ensure the post-order traversal of tree items is ordered correctly
    #     assert tree.items_post_order() == [1, 3, 2, 5, 7, 6, 4]
    #
    # def test_items_level_order_with_7_numbers(self):
    #     # Create a complete binary search tree of 7 items in level-order
    #     items = [4, 2, 6, 1, 3, 5, 7]
    #     tree = KDTree(items)
    #     # Ensure the level-order traversal of tree items is ordered correctly
    #     assert tree.items_level_order() == [4, 2, 6, 1, 3, 5, 7]
    #

if __name__ == '__main__':
    unittest.main()
