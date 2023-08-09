from random import randint
total_sum = 0

for toss in range(0, 10000):
    dice_roll = randint(1, 6)
    total_sum += dice_roll

average = total_sum / 10000

print(f"Total throws: {10000}")
print(f"Total sum: {total_sum}")
print(f"Average: {average:.2f}")