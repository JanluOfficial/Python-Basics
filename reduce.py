from functools import reduce
def combine(number1, number2) -> int:
    return number1 + number2

numbers = [1,2,3,4,5,6,7,8]

## Pre-reduced numbers
print(numbers)

## Reduced numbers
## Final output
print(reduce(combine, numbers))
