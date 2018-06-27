def is_binary_search_tree(root):

   # Determine if the tree is a valid binary search tree
   if root==None:
       return True
   n = root.value
   if root.left!=None:
       temp = root.left
       while temp!=None:
           if temp.value>=n:
               return False
           temp=temp.right
   if root.right!=None:
       temp = root.right
       while temp!=None:
           if temp.value<=n:
               return False
           temp=temp.left
   if root.left==None and root.right==None:
       return True
   if root.left==None:
       return is_binary_search_tree(root.right)
   return is_binary_search_tree(root.left) and is_binary_search_tree(root.right)

   # return True



