def rev(n):
    # Initialize the reversed number
    s = 0
    while n != 0:
        r = n % 10  # Get the last digit
        s = s * 10 + r  # Add it to the reversed number
        n = n // 10  # Remove the last digit from the original number
    return s

# User input
a = int(input("Enter a number: "))
v = rev(a)

if v == a:
    print("It's a Palindrome Number")
else:
    print("It's not a Palindrome Number")
