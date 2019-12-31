import math
import re

# degrees to radian

pi = 22 / 7
degree = float(input("Input degrees: "))
radian = degree * (pi / 180)
print(radian)

# radian to degree

pi = 22 / 7
radian = float(input("Input radians: "))
degree = radian * (180 / pi)
print(degree)

# accept dimensions and calculate area of parallelogram

base = float(input('Length of base: '))
height = float(input('Measurement of height: '))
area = base * height
print("Area is: ", area)


# sum of all divisors

def sum_div(number):
    divisors = [1]
    for i in range(2, number):
        if (number % i) == 0:
            divisors.append(i)
    return sum(divisors)


print(sum_div(8))
print(sum_div(12))

# quadratic


print("Quadratic function : (a * x^2) + b*x + c")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

r = b ** 2 - 4 * a * c

if r > 0:
    num_roots = 2
    x1 = (((-b) + sqrt(r)) / (2 * a))
    x2 = (((-b) - sqrt(r)) / (2 * a))
    print("There are 2 roots: %f and %f" % (x1, x2))
elif r == 0:
    num_roots = 1
    x = (-b) / 2 * a
    print("There is one root: ", x)
else:
    num_roots = 0
    print("No roots, discriminant < 0.")
    exit()

# Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).

def is_allowed_specific_char(string):
    charRe = re.compile(r'[^a-zA-Z0-9.]')
    string = charRe.search(string)
    return not bool(string)


print(is_allowed_specific_char("ABCDEFabcdef123450"))
print(is_allowed_specific_char("*&%@#!}{"))
#Write a Python program that matches a string that has an a followed by zero or more b's.

def text_match(text):
    patterns = 'ab*?'
    if re.search(patterns,  text):
        return 'Found a match!'
    else:
        return('Not matched!')

print(text_match("ac"))
print(text_match("abc"))
print(text_match("abbc"))
