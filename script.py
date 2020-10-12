import math
import sys


# print(sys.version)
# print(sys.executable)

name = input("Your name:?")


def greet(who_to_greet):

    greeting = "Hello, {}".format(who_to_greet)
    return greeting


print(greet(name))

