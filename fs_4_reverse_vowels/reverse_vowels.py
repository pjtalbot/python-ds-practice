def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """

    vowels = set("aeiou")


    new_str_list = []
    saved_vowels = []

    # build list from str with all vowels replaced with ['']
    # save vowels in order they appear

    for char in s:
        if char.lower() not in vowels:
            new_str_list.append(char)
        else:
            new_str_list.append('')
            saved_vowels.append(char)

    saved_vowels.reverse()

    for vowel in saved_vowels:
        new_str_list[new_str_list.index('')] = vowel


    
    return "".join(new_str_list)

            
            

    # save vowel postions





