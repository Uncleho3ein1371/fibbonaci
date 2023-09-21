f_number = 1
s_number = 2
def cfibbo():

    fibbo_number = f_number + s_number
    return fibbo_number, s_number

fibbo_number, s_number = cfibbo()
third_number = fibbo_number

def fibbocycle():
    first_number = s_number
    second_number = third_number
    while first_number>1:
        fibbo_number1 = first_number + second_number
        print(fibbo_number1)
        return fibbo_number1, second_number




fibbocycle()

