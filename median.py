"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]

        #sort the list
        numbers.sort()

        if len(numbers) % 2 == 1:
            #length is odd
            print(numbers[len(numbers)//2])
        else:
            #length is even
            low_middle = len(numbers) // 2
            median = (numbers[low_middle -1 ] + numbers[low_middle])/2
            print(median)

    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
        
