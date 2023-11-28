def intersection(l1, l2):
    """Return intersection of two lists as a new list::

        >>> intersection([1, 2, 3], [2, 3, 4])
        [2, 3]

        >>> intersection([1, 2, 3], [1, 2, 3, 4])
        [1, 2, 3]

        >>> intersection([1, 2, 3], [3, 4])
        [3]

        >>> intersection([1, 2, 3], [4, 5, 6])
        []
    """

    # semi-naive approach
    # l1_set = set(l1)
    # l2_set = set(l2)

    # return list(l1_set & l2_set)

    return list(set(l1) & set(l2))
