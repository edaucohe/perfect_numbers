from enum import Enum
from typing import Any, Callable, List


class Choice(Enum):
    YES = 'y'
    NON = 'n'


# Verifications
def is_integer_positive(number: Any):
    value: int = int(number)
    assert value > 0
    return value


def verify_input(data: Any, parse_function: Callable[[Any], Any]) -> Any:
    while True:
        input_value = input(data)
        try:
            return parse_function(input_value)
        except AssertionError:
            print(f"The written number must be positive.")
        except ValueError:
            print(f"'{input_value}' isn't an accepted data.")


# Inputs
def enter_number():
    number = verify_input("\nEnter an integer number : ", parse_function=is_integer_positive)
    return number


def try_again():
    user_input = verify_input("\nWould you like to try again? (y/n): ", parse_function=Choice)
    return True if user_input == Choice.YES else False


# Output
def display_perfect_numbers(number: int, perfect_numbers: List[int]):
    if perfect_numbers:
        print(f"The list of perfect numbers in the range of number {number} is: {perfect_numbers}")
    else:
        print(f"There is no perfect numbers smaller than {number}")
