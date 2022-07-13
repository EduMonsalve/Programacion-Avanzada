# This code is contributed by
# Shubham Singh(SHUBHAMSINGH10)
# https://www.geeksforgeeks.org/print-binary-tree-2-dimensions/

COUNT = [10]

# Function to print binary tree in 2D
# It does reverse inorder traversal
def print2DUtil(root, space) :

    # Base case
    if (root == None) :
        return

    # Increase distance between levels
    space += COUNT[0]

    # Process right child first
    print2DUtil(root.der, space)

    # Print current node after space
    # count
    print()
    for i in range(COUNT[0], space):
        print(end = " ")
    print(root.info)

    # Process left child
    print2DUtil(root.izq, space)

# Wrapper over print2DUtil()
def print2D(root) :
    
    # space=[0]
    # Pass initial space count as 0
    print2DUtil(root, 0)


