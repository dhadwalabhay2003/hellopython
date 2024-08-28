input_string = input("Enter a sentence: ")
n = int(input("Enter the length of character: "))

words = input_string.split()
long_words = [word for word in words if len(word) > n]

print(words)
