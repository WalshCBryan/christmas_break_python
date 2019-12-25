import multiprocessing
import os


# prints twinkle twinkle properly formatted
print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a "
      "diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")

# accept a users first and last name separately, then concatanate them

first_name = input("Input your First Name : ")
last_name = input("Input your Last Name : ")
print("Hello  " + first_name + " " + last_name)

# accept CSVs from a user an return as a list and as a tuple
values = input("Input some nyums separated by a comma (,) : ")
list = values.split(",")
tuple = tuple(list)
print('List : ', list)
print('Tuple : ', tuple)

# tuples are immutable and cannot be changed once created

# return the first and last value from the following list
color_list = ["Red","Green","White" ,"Black"]

print(color_list[0])
print(color_list[-1])



# write a program to find the greatest common denom for 2 ints

def gcd(x, y):
    denom = 1

    if x % y == 0:
        return y

    for k in range(int(y / 2), 0, -1):
        if x % k == 0 and y % k == 0:
            denom = k
            break
    return denom

print(gcd(12, 17))
print(gcd(4, 6))


print(multiprocessing.cpu_count())
print("Current File Name : ",os.path.realpath(__file__))
