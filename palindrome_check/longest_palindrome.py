'''
A fun mental exercise to find the longest palindrome in a given string.
'''

def main():
    '''
    Primary function
    '''
    string_to_check = input("Input string:")
    string_len = int(len(string_to_check))
    biggest_pal = str()
    for _ in range(0,string_len):
        for __ in range(string_len,_,-1):
            pal_check = string_to_check[_:__]
            if pal_check == pal_check[::-1]:
                if len(pal_check) > len(str(biggest_pal)):
                    biggest_pal = pal_check

    return(biggest_pal, string_to_check)

if __name__ == '__main__':
    result, initial_string = main()
    print(f"Biggest palindrome contained within the string '{initial_string}':")
    print(result)
    print(f"{len(result)} characters long.")
