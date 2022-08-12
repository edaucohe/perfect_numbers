"""
Get perfect numbers of a range.

NB: A perfect number is a positive integer that is equal to
the sum of its positive divisors, excluding the number itself.
For instance, 6 has divisors 1, 2 and 3 (excluding itself).
Because of 1 + 2 + 3 is equal to 6, number 6 is a perfect number.

"""

# In order to get perfect numbers, Euclid-Euler theorem is implemented.

# Euclid-Euler theorem states that an even number is perfect
# if, and only if, it has the form [2^(p-1)]*[2^(p)-1]
# where "2^(p)-1" and "p" are prime numbers.

from typing import List
import math

import views


def is_prime_number(number: int) -> bool:
    # Because of numbers 1 and 2 will return False after loop
    if number <= 3:
        return True

    # Because of factors of a number appears in pairs, the max product is founded
    # when factor a = factor b = square root of number. So we need just iterate
    # until square root of number that we are evaluating.
    square_root_number = math.sqrt(number)
    for iterated_number in range(2, int(square_root_number) + 1):
        # If iterated number cannot divide the number that we are evaluating,
        # (number % iterated_number) == 0 is False and the number is a prime number.
        return False if (number % iterated_number) == 0 else True


def get_perfect_numbers(number: int) -> List[int]:
    perfect_numbers = []
    perfect_number = 0
    p = 2

    while perfect_number < number:
        mersenne = pow(2, p) - 1

        # To get perfect numbers using Euclid-Euler theorem, we need
        # to verify if "p" and "mersenne" are prime numbers.
        p_is_prime: bool = is_prime_number(p)
        mersenne_is_prime: bool = is_prime_number(mersenne)

        # Because both numbers must be simultaneously prime numbers
        if p_is_prime and mersenne_is_prime:
            perfect_number = 2**(p-1)*mersenne
            perfect_numbers.append(perfect_number)

        p += 1

    return perfect_numbers[:-1] if perfect_numbers[-1] > number else perfect_numbers


def main():
    run = True
    while run:
        number: int = views.enter_number()
        perfect_numbers: List[int] = get_perfect_numbers(number=number)
        views.display_perfect_numbers(number, perfect_numbers)

        yes_answer: bool = views.try_again()
        if not yes_answer:
            run = False


if __name__ == "__main__":
    main()
