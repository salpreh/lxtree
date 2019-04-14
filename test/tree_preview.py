# -*- coding: utf-8 -*-
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/..")
from lxtree import TreeNode


def code_sample():
    # Creating root
    root = TreeNode('root')

    # Adding a list of nodes
    root.children = [TreeNode('branch1'), TreeNode('branch3')]

    # Insert node
    root.insert_child(TreeNode('branch2'), 1)

    # Appending to a branch 1 by index
    root[0].append_child(TreeNode('branch11'))

    # Using index to assign children to branch11
    root[0][0] = [TreeNode('leaf111'), TreeNode('leaf112')]

    # Use `set_children` to add nodes as argv
    root[1].set_children(TreeNode('leaf21'), TreeNode('leaf22'), TreeNode('leaf23'))

    # Print tree
    print(root)


def compressed_sample():
    root = TreeNode('root').set_children(
        TreeNode('branch1').append_child(
            TreeNode('branch11').set_children(
                TreeNode('leaf111'),
                TreeNode('leaf112')
            )
        ),
        TreeNode('branch2').set_children(
            TreeNode('leaf21'),
            TreeNode('leaf22'),
            TreeNode('leaf23')
        ),
        TreeNode('branch3')
    )

    print(root)

def test_tree():
    root = TreeNode('root-node')
    root.append_child(TreeNode('leaf1').set_children(
            TreeNode('sub-leaf11'),
            TreeNode('sub-leaf12').append_child(TreeNode('sub-leaf121')),
            TreeNode('sub-leaf13')))
    root.append_child(TreeNode('leaf2'))

    print(root)


if __name__ == '__main__':
    compressed_sample()
