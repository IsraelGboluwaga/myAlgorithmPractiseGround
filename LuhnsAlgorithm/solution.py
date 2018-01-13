#Implementing Luhn's algorithm


def sum_up_and_return_arr_of_digits(n):
    total_sum = 0
    arr = []

    if not isinstance(n, int):
        raise TypeError('Insert a number')

    for no in range(len(str(n))):
        num = int(no)
        num *= 2

        if len(no) > 1:
            arr.append(num)
        else:
            arr.append()

    return arr


print(sum_up_and_return_arr_of_digits(812))


def check_number_x2(num):

    if type(num) == int:
        number = str(num)

    c = []

    for i in range(len(number), -1, -2):
        c.append(i)

    return c #sum_up_and_return_arr_of_digits(c)


def check_number_x1(num):
    number = list(str(num))
    c = []

    for i in range(len(number), -2):
        c.append(i)

    return sum(c)


