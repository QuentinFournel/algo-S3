####################
# 2.1: min and max #
####################


def minBTree(B):
    '''
    B is not empty
    Iterative version (with a loop)
    '''
    while B.children != []:
        B = B.children[0]
    return B.keys[0]


def maxBTree(B):
    '''
    B is not empty
    Recursive version
    '''
    if B.children:
        return maxBTree(B.children[B.nbkeys])  # B.children[-1]
    else:
        return B.keys[B.nbkeys-1]   # B.keys[-1]


##################
# 2.2: Searching #
##################


def __binarySearchPos(L, x, left, right):
    """
    returns the position where x is or should have been in L[left, right[
    """
    if right <= left:
        return right
    mid = left + (right - left) // 2
    if L[mid] == x:
        return mid
    elif x < L[mid]:
        return __binarySearchPos(L, x, left, mid)
    else:
        return __binarySearchPos(L, x, mid+1, right)


def binarySearchPos(L, x):  # will be used in insertions and deletions
    """
    returns the position where x is or should have been in L
    """
    return __binarySearchPos(L, x, 0, len(L))


#################
# 2.3 insertion #
#################


def leftRotation(B, i):
    '''
    makes a rotation from child i+1 to child i
    Conditions:
    - the tree B exists,
    - its child i exists and its root is not a 2t-node,
    - its child i+1 exists and its root is not a t-node.
    '''
    L = B.children[i]
    R = B.children[i+1]

    L.keys.append(B.keys[i])
    B.keys[i] = R.keys.pop(0)
    if R.children:
        L.children.append(R.children.pop(0))


def rightRotation(B, i):
    '''
    makes a rotation from child i-1 to child i
    Conditions:
    - the tree B exists,
    - its child i exists and its root is not a 2t-node,
    - its child i-1 exists and its root is not a t-node.
    '''
    L = B.children[i-1]
    R = B.children[i]

    R.keys.insert(0, B.keys[i-1])
    B.keys[i-1] = L.keys.pop()
    if L.children:
        R.children.insert(0, L.children.pop())


# ------------------------------------------------------------------------------
# merge
def merge(B, i):
    '''
    merge B children i and i+1 into child i
    Conditions:
    - the tree B exists and its root is not a t-node,
    - children i and i+1 exist and their roots are t-nodes.
    '''
    L = B.children[i]
    R = B.children.pop(i+1)  # B.children[i+1]
    L.keys.append(B.keys.pop(i))
    L.keys += R.keys
    L.children += R.children


# -------------------------- delete -------------------------------------------
def __delete(B, x):
    i = binarySearchPos(B.keys, x)

    if B.children == []:  # leaf
        # we're in a leaf, if the to-be-deleted key is here we pop it,
        # otherwise we do nothing
        if i < B.nbkeys \
           and x == B.keys[i]:
            B.keys.pop(i)

    else:  # not a leaf
        if i >= B.nbkeys or x != B.keys[i]:
            # the element is not in this (internal) node

            if B.children[i].nbkeys == B.degree - 1:
                # the child we need to continue in is a t-node, we need to add
                # keys to it by using a rotation or merging it with another
                # node.
                if i > 0 and B.children[i-1].nbkeys > B.degree - 1:
                    # it's left sibling can give a key -> right rotation
                    rightRotation(B, i)
                elif i < B.nbkeys and B.children[i+1].nbkeys > B.degree - 1:
                    # it's right sibling can give a key -> left rotation
                    leftRotation(B, i)
                else:
                    # none of it's immediate siblings can give a key, we need
                    # to merge
                    if i == B.nbkeys:
                        i -= 1
                    merge(B, i)

            __delete(B.children[i], x)

        else:  # we found the element to delete but it's not in a leaf
            if B.children[i].nbkeys > B.children[i+1].nbkeys:
                # left child has more keys than the right one, which also means
                # we could delete one if we need to, so let's overwrite our
                # to-be-deleted key with the maximum of our left child before
                # recursively deleting the original max.
                B.keys[i] = maxBTree(B.children[i])
                __delete(B.children[i], B.keys[i])

            elif B.children[i+1].nbkeys > B.degree - 1:
                # the right child has more or the same number of keys than the
                # left one *and* has enough keys for us to delete one if we
                # have to, so let's overwrite our to-be-deleted key with the
                # minimum of our right child before recursively deleting the
                # original min.
                B.keys[i] = minBTree(B.children[i+1])
                __delete(B.children[i+1], B.keys[i])

            else:
                # none of our two children have enough keys for us to delete
                # one if we need to (they're both t-nodes), so let's merge them
                # as a precaution. After that, our to-be-deleted key has
                # descended to the ith child, so we try again to delete in that
                # child.
                merge(B, i)
                __delete(B.children[i], x)


def delete(B, x):
    if B is not None:
        __delete(B, x)
        if B.nbkeys > 0:
            return B
        elif B.children:
            return B.children[0]
    return None
