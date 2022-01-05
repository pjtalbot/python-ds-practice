def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    dict = {}

    chars = set(phrase)

    for char in chars:
        dict[char] = phrase.count(char)

    return dict

    

    # make set from phrase
    # loop over set, checking count, make dict