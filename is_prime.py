def is_prime(num):
    """Checks if a number is prime.

    Input:
        num (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.

    Example:

    boolean = is_prime(5)   # returns True
    print(boolean)
    """


    # Function implementation here ...
    output = None
    if num == 1:
        output = False
    else:
        num_sqrt = int(num**(1/2))
        if num_sqrt == 1:
            output = True
        else:
            for i in range(2, num_sqrt + 1):
                if num % i == 0 and num != i:
                    output = False
                    break
                output = True
    return output
            
# # # Run code example
# boolean = is_prime(5)   # returns True
# print(boolean)