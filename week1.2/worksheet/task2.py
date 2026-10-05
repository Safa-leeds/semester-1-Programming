def read_numbers():
    """
    Prompts the user to enter a series of numbers on a single line,
    separated from each other by spaces.

    Returns a list of float values corresponding to the numbers that were
    input by the user.
    """
    line = input("Enter some numbers, separated by spaces: ")
    numbers = [float(item) for item in line.split()]
    return numbers
import sys
numbers = read_numbers()
if len(numbers) == 0:
    sys.exit('Error: no numbers provided')
else:
    print(f'Minimum = {min(numbers)}')
    print(f'Maximum = {max(numbers)}')
    print(f'Mean = {'{:.1f}'.format(sum(numbers)/ len(numbers))}')
    numbers.sort()
    if len(numbers) % 2 == 0:
        mid_right = int(len(numbers)/2)
        mid_left = mid_right -1
        print(f'Median = {(numbers[mid_right] + numbers[mid_left])/2}')

    else:
        mid = len(numbers)//2
        middle = numbers[mid]
        print(f'Median = {middle}')



