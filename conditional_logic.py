word_in = input("Please write a word:")
if len(word_in) < 5:
    print("Your word is less than 5 characters")
elif len(word_in) > 5:
    print("Your word is greater than 5 characters")
else:
    print("Your word has 5 characters")