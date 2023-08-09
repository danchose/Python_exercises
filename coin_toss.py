from random import randint

trials = 10000
flips = 0

for trial in range(0, trials):
    firstflip = randint(0, 1)
    flips += 1
    while randint(0, 1) == firstflip:
        flips += 1
    flips += 1

print("The average number of coin flips was {}".format(flips/trials))

