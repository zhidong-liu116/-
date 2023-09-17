### leetcode226翻转二叉树，前序遍历+后序遍历的写法

```py
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 中，左，右。这个遍历顺序就是“前序遍历”
        if root is None: return None
        # temp = root.right
        # root.right = root.left
        # root.left = temp
        root.left, root.right = root.right, root.left # 中
        self.invertTree(root.left) # 左
        self.invertTree(root.right) # 右
        return root

        # 左，右，中。这个遍历顺序就是“后序遍历”
        '''
        if root is None:
            return None
        self.invertTree(root.left) # 左
        self.invertTree(root.right) # 右
        root.left, root.right = root.right, root.left # swap左右节点的过程， 中
        # 函数返回时就表示当前这个节点，以及它的左右子树
		# 都已经交换完了
        return root
        '''
```
