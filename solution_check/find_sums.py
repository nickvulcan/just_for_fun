'''
An exercise to find two numbers that add up to a target in a list of integers.
'''
import sys

nums = []
TARGET = int()
try:
    TARGET = int(input("Enter a target:  "))
except ValueError:
    print("That's not a number!")
if not TARGET:
    print("User error.  Replace user.  Fatal error - exiting.")
    sys.exit()


print("Input a blank line to end the list.")
while True:
    try:
        print(f"The list so far:  {nums}")
        entry = int(input("Enter a number:  "))
    except ValueError:
        print("That's not a number!")
        break
    nums.append(entry)


print(nums)
for first_index, num in enumerate(nums):
    for second_index, other_num in enumerate(nums):

        if nums[first_index] + nums[second_index] == TARGET:
            print(f"Found it!  The answer was:  {first_index}, {second_index}")
            print(f"The solution is {nums[first_index]} and {nums[second_index]}.")
            sys.exit()
print("The answer was not found.")
