f_number = 1
s_number = 2
def cfibbo():
    fibbo_number = f_number + s_number
    return fibbo_number, s_number


fibbo_number, s_number = cfibbo()
third_number = fibbo_number

def fibbocycle():
    your_range = int(input("please provide your favorite range: "))
    while your_range<1:
        your_range = int(input("please provide a number higher than 1: "))
    print(f_number)
    first_number = s_number
    print(first_number)
    second_number = third_number
    print(second_number)
    while second_number<your_range:
        fibbo_number1 = first_number + second_number
        print(fibbo_number1)
        first_number = second_number
        second_number = fibbo_number1








fibbocycle()

