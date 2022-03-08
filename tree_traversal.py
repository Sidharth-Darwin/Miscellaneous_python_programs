# Python program that does tree traversal using preorder, inorder and postorder 

def main()->None:
    tree = input("Enter your tree: ")
    tree = tree.split(sep=',')
    print(tree)
    while(True):
        choice = int(input("Enter 1 for preorder, 2 for inorder and 3 for postorder: "))
        if (choice==1):
            preorder(tree,0)
        elif(choice==2):
            inorder(tree,0)
        elif(choice==3):
            postorder(tree,0)
        else:
            break

def preorder(tree,parent)->None:
    if ((len(tree)-1)>=parent):
        if (tree[parent]!=''):
            print(tree[parent])
        preorder(tree,2*parent+1)
        preorder(tree,2*parent+2)
def inorder(tree,parent)->None:
    if ((len(tree)-1)>=parent):
        inorder(tree,2*parent+1)
        if (tree[parent]!=''):
            print(tree[parent])
        inorder(tree,2*parent+2)
def postorder(tree,parent)->None:
    if ((len(tree)-1)>=parent):
        postorder(tree,2*parent+1)
        postorder(tree,2*parent+2)
        if (tree[parent]!=''):
            print(tree[parent])

if (__name__=="__main__"):
    main()
