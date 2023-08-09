
"""while True:
    user_input = input("Please enter some text: ")
    for letter in user_input:
        if letter == "q":
            break
        elif letter == "Q":
            break
    else:
        print("There is no q or Q in your text")
"""        
"""
while True:
    user_input = input("Please enter some text (type 'q' or 'Q' to quit): ")
    if 'q' in user_input.lower():
        break
    else:
        print("You entered:", user_input)
        
print("Exiting the program. Goodbye!")

"""

for i in range(1, 50):
    if i % 3 == 0:
        continue
    print(i)
    
