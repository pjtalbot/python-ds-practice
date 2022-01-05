def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    counter = {}
    

    for num in nums:
        count = 0
        
        for y in nums:
            if num == y:
                count += 1
        nums.remove(num)
        counter[num] = count
    
    for counts in counter:
        counter.get(counts)

    MAX_KEY = max(counter, key=counter.get)
    return MAX_KEY

        

