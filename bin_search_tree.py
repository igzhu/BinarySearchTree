class Node(object):
    def __init__(self, val):
        self.l_child = None
        self.r_child = None
        self.val = val

    def __str__(self):
      str_self = f'{self.l_child.val if self.l_child  else 0,self.val if self else 0, self.r_child.val if self.r_child else 0}'
      return str_self if str_self else 'non'


class BinarySearchTree(object):
    def insert(self, root, node):
        if root is None:
            #print(node)
            #print(node.val, node.l_child.val if node.l_child else 0, node.r_child.val if node.r_child else 0)
            return node
        if root.val < node.val:
            #print(node.val, node.l_child.val if node.l_child else 0)
            root.r_child = self.insert(root.r_child, node)

            #print(root.r_child)
        else:
            root.l_child = self.insert(root.l_child, node)
            #print(node.r_child.val if node.r_child else 0)
            #print(root.l_child)
        #print(root.val,node.l_child.val if node.l_child else 0, node.r_child.val if node.r_child else 0)
        print(root)
        return root

    def in_order_place(self, root):
        if not root:
            return None
        else:
            self.in_order_place(root.l_child)
            print(root)
            #print(root.val)
            self.in_order_place(root.r_child)

    def pre_order_place(self, root):
        if not root:
            return None
        else:
            print(root)
            #print(root.val)

            self.pre_order_place(root.l_child)
            self.pre_order_place(root.r_child)

    def post_order_place(self, root):
        if not root:
            return None
        else:
            self.post_order_place(root.l_child)
            self.post_order_place(root.r_child)
            #print(root.val)
            print(root)


""" Create different node and insert data into it"""
r = Node(9)
nodes = BinarySearchTree()
nodeList = [1, 8, 5, 12, 14, 6, 15, 7, 16, 8]
for nd in nodeList:
    nodes.insert(r, Node(nd))
    #print(a,a.l_child.val if a.l_child else 0, a.r_child.val if a.r_child else 0)


print("------In order ---------")
print(nodes.in_order_place(r))

print("------Pre order ---------")
print(nodes.pre_order_place(r))

print("------Post order ---------")
print(nodes.post_order_place(r))

