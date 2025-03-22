import re 

def prime_numbers(int_x, int_y):

    """Outputs all of the prime numbers between the two integers supplied as arguments

    Args:
        int_x, int_y: Two positive integers supplied as arguments
    Returns:
        list: A list of all prime numbers between two positive integers supplied as arguments inclusive of arguments if prime
        In the event the argument passed is inappropriate an error message is outputted
    """

    int_a = 0
    int_b = 0

    if int_x < int_y:
        int_a = int_x 
        int_b = int_y 
    else:
        int_a = int_y
        int_b = int_x 

    lst_prime_numbers = []
    for val in range(int_a, int_b + 1):
        lst_factors = []
        for val_ii in range(1, val + 1):
            if val % val_ii == 0:
                lst_factors.append(val_ii)
        
        if len(lst_factors) == 2:
            lst_prime_numbers.append(val)
    
    n = 10
    lst_prime_numbers_chunks_of_ten = [lst_prime_numbers[i: i + n] for i in range(0, len(lst_prime_numbers), n)]
    for ele in lst_prime_numbers_chunks_of_ten:
        print(f"Number of values in this output statement: {len(ele)} - {ele}")
    return lst_prime_numbers_chunks_of_ten


def main():
    regex = re.compile(r'[0-9]+')
    str_x = input("Enter your first positive integer:\n>")
    str_y = input("Enter your second positive integer:\n>")

    result_x = regex.fullmatch(str_x)
    result_y = regex.fullmatch(str_y)

    if result_x and result_y:
        int_x = int(str_x)
        int_y = int(str_y)
        prime_numbers(int_x, int_y)
    else:
        print("At least one of the values you have entered are inappropriate")

main()