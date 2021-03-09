"""
Given a binary tree t and an integer s, determine whether there is a root to leaf path in t such that the sum of vertex values equals s.

t = {
    "value": 4,
    "left": {
        "value": 1,
        "left": {
            "value": -2,
            "left": null,
            "right": {
                "value": 3,
                "left": null,
                "right": null
            }
        },
        "right": null
    },
    "right": {
        "value": 3,
        "left": {
            "value": 1,
            "left": null,
            "right": null
        },
        "right": {
            "value": 2,
            "left": {
                "value": -2,
                "left": null,
                "right": null
            },
            "right": {
                "value": -3,
                "left": null,
                "right": null
            }
        }
    }
}
and
s = 7,
the output should be hasPathWithGivenSum(t, s) = true.
Path 4 -> 3 -> 2 -> -2 gives us 7, the required sum.
"""


class Tree(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None


def hasPathWithGivenSum(t, s):
    # if you have treversed all the way down the tree and have not found a path return False
    if t == None:
        return False
    # if you reach and a leaf node and the s - the node's value == 0 return True because there is a valid path
    elif t.left == None and t.right == None and s - t.value == 0:
        return True
    else:
        # otherwise recurssively call the function on the trees left and right nodes and subtract the value of s for each node's value
        return hasPathWithGivenSum(t.left, s - t.value) or hasPathWithGivenSum(
            t.right, s - t.value
        )
