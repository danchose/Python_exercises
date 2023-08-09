num_in = input("Enter a positive integer:")
num_in = int(num_in)
if num_in < 0:
    print("I said positive integer, you IDIOT!")
i = 1
for i in range(i, num_in+1):
    if num_in % i == 0:
        print("{} is a divisor of {}".format(i, num_in))
    i = i + 1



