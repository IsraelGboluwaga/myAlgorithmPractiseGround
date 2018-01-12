#Codility


# For example, given N = 1041 the function should return 5, because N has binary representation
# 10000010001 and so its longest binary gap is of length 5.

maxNum = 2147483647


def binary_gap(N):
    if not isinstance(N, int):
        raise TypeError('Not an integer')
    if N < 1:
        raise ValueError('Only positive numbers allowed')
    if N > maxNum:
        raise ValueError('Number ust not be greater than ' + str(maxNum))

    binary_string = str(bin(N)[2:])
    count = 0
    max_count = None
    was_zero = None

    for number in range(len(binary_string)):
        is_zero = number == '0'

        if bool(was_zero) == is_zero:
           count += 1

        else:
            if max_count is None:
                max_count = 0
            elif count > max_count:
                max_count = count
            count = 1

        was_zero = is_zero

    if max_count is None:
        max_count = 0
        return max_count

    return max_count

