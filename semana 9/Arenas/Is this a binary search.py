class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def newNode():
    temp = node(-1)
    temp.left = None
    temp.right = None
    return(temp);

""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
def check_binary_search_tree_(root):
    def is_valid(node, min_val, max_val):
        if node is None:
            return True
        
        if not (min_val < node.data < max_val):
            return False
        
        return (is_valid(node.left, min_val, node.data) and 
                is_valid(node.right, node.data, max_val))

    return is_valid(root, -1, 10001)
ht = int(input())
cnt = 0
values = map(int, input().split(' '))
values = list(values)
root  = newNode()
def inorder(root, ht):
    global cnt
    global values
    if cnt == len(values):
        return
    else:
        if(ht>0):
            root.left = newNode();
            inorder(root.left, ht-1);
        root.data = values[cnt];
        cnt+=1
        if(ht>0):
            root.right = newNode();
            inorder(root.right, ht-1);
inorder(root, ht);
if(check_binary_search_tree_(root)):
    print("Yes")
else:
    print("No")