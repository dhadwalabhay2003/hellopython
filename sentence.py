input_string = input("Enter a Sentence: ")
n = int(input("Enter the Length : "))

words = input_string.split()
long_words = [word for word in words if len(word) > n]

print(f"Words longer than {n} characters: {long_words}")
