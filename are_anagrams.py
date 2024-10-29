def are_anagrams(str1, str2):
    """
    This function checks if two strings are anagrams of each other.

    Parameters:
    ----------
    str1 : str
        The first string to be compared.
    str2 : str
        The second string to be compared.

    Returns:
    -------
    bool:
        Returns True if the two strings are anagrams, otherwise False.

    Example:
    --------
    are_anagrams("listen", "silent")  # Output: True
    are_anagrams("hello", "world")    # Output: False
    """

    # Function implementation here ...
    str1_list = list(str1)
    str2_list = list(str2)
    for letter in str1:
        if str1_list.__contains__(letter) and str2_list.__contains__(letter):
            str1_list.remove(letter)
            str2_list.remove(letter)
    output = True if len(str1_list) == 0 and len(str2_list) == 0 else False
    return output

## Example 
# print(are_anagrams("listen", "silent"))  # Expected output: True
# print(are_anagrams("hello", "world"))    # Expected output: False
# print(are_anagrams("ate", "eat"))
# print(are_anagrams("heart", "earth"))
# print(are_anagrams("heatt", "eahth"))