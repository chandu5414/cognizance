'''
Write a python program to accept a string from the user and display characters, that are present at an even index number.
'''

# read a string
str = input("Enter a string\n")
# create a string with characters at multiples of 2
modified_string = str[::2]
print(modified_string)
