# imports
from bst import BST

# BST instantiation
bst = BST()

# assert bst.search_iterative(5) == True
# assert bst.search_iterative(20) == False
# print(bst.search_iterative(5))
# print(bst.search_recursive(20))

assert bst.level_order() == [7, 4, 9, 2, 5, 8, 12, 0, 16]
print(bst.level_order())
# assert bst.pre_order()   == [7, 4, 2, 0, 5, 9, 8, 12, 16]
# assert bst.in_order()    == [0, 2, 4, 5, 7, 8, 9, 12, 16]
# assert bst.post_order()  == [0, 2, 5, 4, 8, 16, 12, 9, 7]
# write your assertions below
# format
# assert function_call == expected_output
# If the test passes → no output
# If it fails → AssertionError is shown
