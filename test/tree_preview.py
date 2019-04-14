# -*- coding: utf-8 -*-
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/..")
from lxtree import TreeNode

if __name__ == '__main__':
    root = TreeNode('root-node')
    root.append_child(TreeNode('leaf1').set_children(
            TreeNode('sub-leaf11'),
            TreeNode('sub-leaf12').append_child(TreeNode('sub-leaf121')),
            TreeNode('sub-leaf13')))
    root.append_child(TreeNode('leaf2'))

    print(root)
