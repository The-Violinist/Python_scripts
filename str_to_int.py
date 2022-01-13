# This is a function do demonstrate changing data type witout using the int function

num = "12345"

def int_conversion(num):
    total = 0
    i = 1
    power = 10 ** (len(num) - i)
    for item in num:
        x = (ord(item) - 48) * power
        total += x
        i += 1
        power = 10 ** (len(num) - i)
    return total

print(int_conversion(num))