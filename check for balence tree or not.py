#susovan

from height import height


class Node:
    def __init__(self, key):
        self.key=key
        self.right=None
        self.left=None




def isBalence(root):
    if root!=None:
        return 0
    lh=height(root.left)
    rh=height(root.right)

    return abs(lh-rh)<=1 and isBalence(root.left) and isBalence(root.right)

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.right.left = Node(50)
root.right.right = Node(60)
root.right.left.left = Node(70)
root.right.left.right = Node(80)


print(isBalence(root))

