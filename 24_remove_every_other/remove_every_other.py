def remove_every_other(lst):
    """Return a new list of other item.

        >>> lst = [1, 2, 3, 4, 5]

        >>> remove_every_other(lst)
        [1, 3, 5]

    This should return a list, not mutate the original:

        >>> lst
        [1, 2, 3, 4, 5]
    """

    # my solution (bad, wouldn't work if list has duplicates)

    new_list = []

    for item in lst:
        if (lst.index(item) % 2 == 0):
            new_list.append(item)
    
    return new_list

    # better solution

    # return lst[::2]

    