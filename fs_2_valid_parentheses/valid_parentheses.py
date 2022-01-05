def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """

    # if starting at closed parense or ending at open parens, automatic False

    if parens[0] == ")" or parens[-1] == "(":
        return False

    # if number of parense is odd, automatic false

    if len(parens) % 2 != 0:
        return False

    
    for i in range(len(parens)/2):
        if parens[i] == parens[-1 - i]:
            return False

    