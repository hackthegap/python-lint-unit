# we need an agreement about margins, spacements, and so on:

# PEP8
# company standart


def sayHello():  # java and Javascript style
    print("Hello, again!")


def say_hello():
    print("Hello, again!")  # identation: 4 spaces


def sum(first_number, second_number):
    return first_number + second_number


# line limit: 79
# variable or functions: lower_case
# constant: UPPER_CASE
# class name: MyClassName, Employee, BankAccount
# private variable: _internal_counter

# lint tools: audit your code and search for things not following the PEP8
# python lint will show you the points where you need to fix the code according with PEP8
# black will fix you small errors, like white spaces, margins, etc. 

sayHello()
sum(1, 6)
