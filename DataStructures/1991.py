N = int(input())

tree = {}

for _ in range(N):
    data, left, right = input().split()
    tree[data] = [left, right]

def preorder(root):
    if root == '.':
        return ""
    node = tree[root]
    return root + preorder(node[0]) + preorder(node[1])

def inorder(root):
    if root == '.':
        return ""
    node = tree[root]
    return inorder(node[0])+ root + inorder(node[1]) #left

def postorder(root):
    if root == '.':
        return ""
    node = tree[root]
    return postorder(node[0]) + postorder(node[1]) + root #left
    
print(preorder('A'))
print(inorder('A'))
print(postorder('A'))