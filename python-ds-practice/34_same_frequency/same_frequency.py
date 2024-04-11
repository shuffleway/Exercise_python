def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
   
# Convert the numbers to strings
    str_num1 = str(num1)
    str_num2 = str(num2)
    
    # Create dictionaries to store digit frequencies
    freq1 = {n: str_num1.count(n) for n in str_num1}
    freq2 = {n: str_num2.count(n) for n in str_num2}
    
    # Check if the dictionaries are equal
    return freq1 == freq2
