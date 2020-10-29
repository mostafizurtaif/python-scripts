import random

def rand_int_seq(n_digit, from_inc, to_inc):
    rand_int_seq = ''
    
    for count in range(n_digit):
        rand_int = str(random.randint(from_inc, to_inc))
        rand_int_seq += rand_int
    
    return rand_int_seq


def rand_int_list(n_items, from_inc, to_inc):
    rand_int_list = []

    for count in range(n_items):
        rand_int = random.randint(from_inc, to_inc)
        rand_int_list.append(rand_int)

    return rand_int_list

