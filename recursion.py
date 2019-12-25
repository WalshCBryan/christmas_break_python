# Write a Python program to calculate the sum of a list of numbers.


def list_sum(num_List):
    if len(num_List) == 1:
        return num_List[0]
    else:
        return num_List[0] + list_sum(num_List[1:])


print(list_sum([2, 4, 5, 6, 7]))  # 24
print(list_sum([1, 2, 3, 4, 10]))  # 20


# Write a Python program to converting an integer to a string in any base.

def to_string(n, base):
    convert_String = "0123456789ABCDEF"
    if n < base:
        return convert_String[n]
    else:
        return to_string(n // base, base) + convert_String[n % base]


print(to_string(2835, 16))
