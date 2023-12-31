def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of items.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """

    counter = {}

    for num in nums:
        counter[num] = counter.get(num, 0) + 1

    # max_count = max(counter.values())
    max_count = 0
    max_count_num = None

    # parens optional and could be easier to read
    for (num, count) in counter.items():
        if count > max_count:
            max_count = count
            max_count_num = num

    return max_count_num
