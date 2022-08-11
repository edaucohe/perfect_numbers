"""
Get perfect numbers of a range.

NB: A perfect number is a positive integer that is equal to
the sum of its positive divisors, excluding the number itself.
For instance, 6 has divisors 1, 2 and 3 (excluding itself).
Because of 1 + 2 + 3 is equal to 6, number 6 is a perfect number.

"""

# I pretend to use algorithms to optimize the script.
# In another way, it could have a lot of numbers to loop.

# So, I will use Euclid-Euler theorem for this purpose.

# Euclid-Euler theorem states that an even number is perfect
# if, and only if, it has the form [2^(p-1)]*[2^(p)-1]
# where "2^(p)-1" and "p" are prime numbers.

from typing import List, Any
import math


NUMBER: int = 30


def is_integer_positive(number: Any):
    try:
        value: int = int(number)
        assert value > 0
        return value
    except AssertionError:
        print(f"Number {number} must be an integer positive.")
    except ValueError:
        print(f"Data '{number}' must be a number.")


def is_prime_number(number: int) -> bool:
    # Because of numbers 1 and 2 will return False after loop
    if number <= 3:
        return True

    # Because of factors of a number appears in pairs, the max product is founded
    # when factor a = factor b = square root of number. So we need just iterate
    # until square root of number we are evaluating.
    # NB: We have two factors because we use module "%" in "if" condition to know
    # if an iterated number can divide the number that we are evaluating.
    square_root_number = math.sqrt(number)
    for iterated_number in range(2, int(square_root_number) + 1):
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
    positive_number = is_integer_positive(NUMBER)

    try:
        perfect_numbers: List[int] = get_perfect_numbers(number=positive_number)
        if perfect_numbers:
            print(f"The list of perfect numbers smaller than {positive_number} is: {perfect_numbers}")
        else:
            print(f"There is no perfect numbers smaller than {positive_number}")
    except TypeError:
        print("In this case, script cannot get perfect numbers.")


if __name__ == "__main__":
    main()
