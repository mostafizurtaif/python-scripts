import random

def gen_rand_numseq(dgt_num, frm_inc, to_inc):
    rand_numseq = ''

    for i in range(dgt_num):
        rand_int = random.randint(frm_inc, to_inc)
        rand_int = str(rand_int)
        rand_numseq += rand_int

    return rand_numseq
