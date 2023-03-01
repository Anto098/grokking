from __future__ import print_function


class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end='')
            temp = temp.next
        print()


def sum_square_all_digits(num):
    return sum([int(c) ** 2 for c in str(num)])


def find_happy_number(num):
    n1, n2 = num, sum_square_all_digits(num)
    while n1 != n2:
        n1 = sum_square_all_digits(n1)
        n2 = sum_square_all_digits(sum_square_all_digits(n2))

    return n1 == 1


if __name__ == "__main__":
    print(find_happy_number(23))
    print(find_happy_number(12))
