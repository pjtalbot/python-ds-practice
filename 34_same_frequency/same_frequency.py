def make_counter_dict(nums):
    dict = {}

    key_set = set(str(nums))

    for num in key_set:
        dict[num] = str(nums).count(num)

    return dict

def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    if len([*str(num1)]) is not len([*str(num2)]):
        return False

    num1_dict = make_counter_dict(num1)
    num2_dict = make_counter_dict(num2)
    
    return num1_dict == num2_dict

    # convert to string

    # create frequency counter dict 1 and dict 2 of each num


