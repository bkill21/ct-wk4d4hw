from BST import BinarySearchTree

def list_to_bst(func):
    def wrapper(*args):
        source = func(*args)
        root = source[len(source) // 2] #Declare root at approximate middle of list
        source.remove(root) #Remove the root value from list to prevent creation of same node twice
        bst = BinarySearchTree(root)
        for num in source:
            bst.add_node(num)
        print(f'BST Root value: {bst.root.value}')
        print(f'BST Max value: {bst.get_max()}')
        print(f'BST Min value: {bst.get_min()}')
    return wrapper

@list_to_bst
def create_list(num):
    num_list = []
    for i in range(0, num + 1):
        num_list.append(i)
    return num_list

my_bst = create_list(222)

