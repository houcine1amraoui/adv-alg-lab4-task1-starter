class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        # Pre-built BST (same as bst.png)
        self.root = Node(7)
        self.root.left = Node(4)
        self.root.right = Node(9)
        self.root.left.left = Node(2)
        self.root.left.right = Node(5)
        self.root.right.left = Node(8)
        self.root.right.right = Node(12)
        self.root.left.left.left = Node(0)
        self.root.right.right.right = Node(16)

    # ITERATIVE SEARCH (complete from comments)
    def search_iterative(self, value):
        # 1. Start from the root
        # 2. While current is not None:
        #       - If value matches current node → return True
        #       - If value < current.value → go left
        #       - Else → go right
        # 3. If loop ends → value not found → return False
        pass

    # RECURSIVE SEARCH (complete from comments)
    def search_recursive(self, value):
        # Define helper _search(node, value):
        #   1. If node is None → return False
        #   2. If value matches node.value → return True
        #   3. If value < node.value → search left subtree
        #   4. Else → search right subtree
        #
        # Call helper on the root and return result
        pass

    # LEVEL ORDER TRAVERSAL (BFS)
    def level_order(self):
        # 1. If tree is empty → return empty list
        # 2. Create a queue list
        # 3. Add the root to the queue
        # 4. Create an empty results list
        #
        # 5. While queue is not empty:
        #       - Pop first element
        #       - Add its value to result list
        #       - If left child exists → append to queue
        #       - If right child exists → append to queue
        #
        # 6. Return result list
        pass

    # PRE-ORDER (Root → Left → Right)
    def pre_order(self):
        # Define helper:
        #   1. If node is None → return
        #   2. Visit node value
        #   3. Traverse left subtree
        #   4. Traverse right subtree
        #
        # Call helper on root
        pass

    # IN-ORDER (Left → Root → Right)
    def in_order(self):
        # Define helper:
        #   1. If node is None → return
        #   2. Traverse left subtree
        #   3. Visit node value
        #   4. Traverse right subtree
        #
        # Call helper on root
        pass

    # POST-ORDER (Left → Right → Root)
    def post_order(self):
        # Define helper:
        #   1. If node is None → return
        #   2. Traverse left subtree
        #   3. Traverse right subtree
        #   4. Visit node value
        #
        # Call helper on root
        pass
