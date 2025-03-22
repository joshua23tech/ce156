import string 

def fun1(str_param):
    """Takes a String as an argument and returns True if and only if the String is a palindrome

    Args:
        String: A String value supplied as an argument
    Returns:
        boolean: True if the String is a palindrome; false if the String is not
    """
    str_param_stripped = str_param.replace(" ", "")
    return str_param_stripped == str_param_stripped[::-1]


def fun2(str_param):

    """Takes a String as an argument and returns the second most frequent letter or digit

    Args:
        String: A String value supplied as an argument
    Returns:
        String: A String value representing the second most frequent letter or digit from the String argument supplied
    """

    str_param_upper = str_param.upper() 
    dict_digits_letters = {}
    lst_str_digits = [str(i) for i in range(0, 10)]
    lst_str_letters = list(string.ascii_uppercase)

    for ele_param_upper in str_param_upper:
        if ele_param_upper in dict_digits_letters.keys() or ele_param_upper in dict_digits_letters.keys():
            str_ele_param_upper = str(ele_param_upper)
            dict_digits_letters[str_ele_param_upper] = dict_digits_letters[str_ele_param_upper] + 1
        elif ele_param_upper in lst_str_digits or ele_param_upper in lst_str_letters:
            str_ele_param_upper = str(ele_param_upper)
            dict_digits_letters[str_ele_param_upper] = 1
    
    dict_swapped = {v: k for k, v in dict_digits_letters.items()} 
    lst_int_sorted = sorted(dict_swapped.keys())
    int_second_most_frequent_index = lst_int_sorted[-2]

    str_second_most_freq = dict_swapped[int_second_most_frequent_index]
    return str_second_most_freq


def fun3(str_param):

    """Takes a String as an argument and returns the number of uppercase letters, lowercase letters and digits in the String

    Args:
        String: A String value supplied as an argument
    Returns:
        Tuple: A Tuple containing three values representing the number of uppercase letters, lowercase letters and digits counted in the argument String
    """

    int_upper_count = 0 
    int_lower_count = 0 
    int_digit_count = 0 

    for char in str_param:
        if char.isupper():
            int_upper_count += 1 
        elif char.islower():
            int_lower_count += 1 
        elif char.isdigit():
            int_digit_count += 1 

    return (int_upper_count, int_lower_count, int_digit_count) 

