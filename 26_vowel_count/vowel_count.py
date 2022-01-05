def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowels = set('aeiou')
    count_dict = {}

    for ltr in phrase.lower():
        counter = 0
        if ltr in vowels:
            for i in phrase.lower():
                if ltr == i:
                    counter += 1
            count_dict[ltr] = counter
    
    return count_dict