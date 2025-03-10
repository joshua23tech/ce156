import string 

def fun1(str_param):
    str_param_stripped = str_param.replace(" ", "")
    return str_param_stripped == str_param_stripped[::-1]



def fun2(str_param):
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
    pass 

print(fun1("a bcba"))
print(fun2("sjgosdnosdngsdlgsld2222222222999999999"))