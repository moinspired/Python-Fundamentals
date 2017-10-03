# Odd/Even:
# Create a function called odd_even that counts from 1 to 2000. As your loop executes have your program print the number of that iteration and specify whether it's an odd or even number.


# def odd_even():
#     for i in range(1, 21):
#         if(i % 2 == 1):
#             print "Number is " + str(i) + "." + " This is an odd number."
#         else:
#             print "Number is " + str(i) + "." + " This is an even number."


# odd_even()

# Multiply:
# Create a function called 'multiply' that iterates through each value in a list (e.g. a = [2, 4, 10, 16]) and returns a list where each value has been multiplied by 5.

# The function should multiply each value in the list by the second argument. For example, let's say:


def multiply(a, num):
    for i in range(0, len(a)):
        a[i] = a[i] * num
    print a


# multiply([2, 4, 10, 16], 5)


# Hacker Challenge:
# Write a function that takes the multiply function call as an argument. Your new function should return the multiplied list as a two-dimensional list. Each internal list should contain the 1's times the number in the original list. Here's an example:


def layered_multiples(arr):
    new_array = []
    new = []
    arr = [6, 12, 15]
    for i in range(0, len(arr)):
        for j in range(0, arr[i]):
            new.append(1)
        new_array.append(new)
    print new_array


layered_multiples(multiply([2, 4, 5], 3))
print x
