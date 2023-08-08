def ftoc(fahren):
    result = (int(fahren)-32)*5/9
    return result

def ctof(celsi):
    result = (int(celsi)*9/5)+32
    return result

input_tf = input("Enter your temperature degree in Fahrenheit to convert to Celsium: ")
input_tc = input("Enter your temperature degree in Celsium to convert to Fahrenheit: ")
a = ftoc(input_tf)
b = ctof(input_tc)
print("{} degrees F = {} degrees C".format(input_tf, a))
print("{} degrees C = {} degrees F".format(input_tc, b))