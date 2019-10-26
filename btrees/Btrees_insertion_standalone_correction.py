from algopy.btree import BTree


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

def split(B, i):
    '''
    splits the child i of B
    conditions:
    - B is a nonempty tree and its root is not a 2t-node.
    - The child i of B exists and its root is a 2t-node.
    There is no need to return B, the root (the reference) does not change!
    '''
    mid = B.degree-1
    L = B.children[i]
    R = BTree()

    # keys
    (L.keys, x, R.keys) = (L.keys[:mid], L.keys[mid], L.keys[mid+1:])

    # children
    if L.children == []:  # L and R are leaves, no need to use sublists
        R.children = []
    else:
        (L.children, R.children) = (L.children[:mid+1], L.children[mid+1:])

    # root
    B.keys.insert(i, x)
    B.children.insert(i+1, R)


def __insert(B, x):
    '''
    conditions:
    - B is a nonempty tree
    - its root is not a 2t-node
    returns: nothing. There is no need to return B because the root (the
    reference) does not change, only its attributes do.
    '''
    i = binarySearchPos(B.keys, x)

    if i < B.nbkeys and B.keys[i] == x:  # the inserted key already exists
        return

    elif B.children == []:  # leaf
        B.keys.insert(i, x)
        return

    else:  # a recursive call is needed
        if B.children[i].nbkeys == 2 * B.degree - 1:  # the child is full
            if B.children[i].keys[B.degree-1] == x:
                # the key that would ascend if we split the child is the one we
                # wanted to insert, we can quit right away
                return

            split(B, i)

            if x > B.keys[i]:
                # the split created a new child, if the key we want to insert
                # is greater than the one that ascended during the split, we
                # need to descend into that new child (i+1), not i.
                i += 1

        __insert(B.children[i], x)


def insert(B, x):
    '''
    inserts x in B (if not already in B)
    returns B (needed: in case of new root!)
    '''
    if B.nbkeys == 2 * B.degree - 1:  # the root is full
        B = BTree([], [B])
        split(B, 0)

    __insert(B, x)

    return B
