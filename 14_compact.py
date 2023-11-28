def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """

    # Naive approach
    # truthy_lst = []

    # for element in lst:
    #     if element:
    #         truthy_lst.append(element)

    # return truthy_lst

    return [element for element in lst if element]
