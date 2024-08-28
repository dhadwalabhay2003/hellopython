n = int(input("Enter the number: "))
reversed = 0
while(n>0):
    remainder = n%10
    reversed = (reversed*10)+remainder
    n = n // 10

print(f"Reversed number:{reversed}")
