'''
This is a quick mental exercise to check whether an integer (or string) is a palindrome.
'''
PAL_CHECK = input()
PAL_CHECK = str(PAL_CHECK)
if PAL_CHECK[::-1] == PAL_CHECK:
    print("The input is a palindrome.")
else:
    print("The input is NOT a palindrome.")
