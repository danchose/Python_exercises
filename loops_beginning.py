"""
n = 1
while (n < 5):
    print("n =", n)
    n = n + 1
print("Loop finished")

for n in range(1, 5):
    print("n =", n)
print("Loop finished")

for n in range(1, 4):
    for j in ["a", "b", "c"]:
        print("n =", n, "and j =", j)



for n in range(2, 11):
    print("n =", n)

i = 2 
while (i < 11):
    print("i =", i)
    i = i + 1
"""

def doubles(num):
    i = 1
    while (i < 4):
        num = num * 2
        print(num)
        i = i + 1

input_num = input("Enter some number: ")
doubles(int(input_num))
