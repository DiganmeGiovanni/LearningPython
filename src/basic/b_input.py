""" Use input demo """
#
# input()  function is used to receive input from the console,
# accepts an optional string argument called prompt  and returns a string.

name = input('Enter your name: ')
print('Your name is: ', name)

#
# Note that input()  returns string even if you enter a number,
# to convert it to an integer you can use int() or eval().

age = int(input("\nEnter your age: "))
print('Your age is: ', age)
