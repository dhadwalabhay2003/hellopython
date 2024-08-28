#sum of digits
n = int(input("Enter the digits: "))
s = 0
while(n!=0):
    r = n % 10
    s = s + r
    n = n // 10
print("Sum of the digits is: ", s)
print("//////////////////////////////")  
#reverse of the number
n = int(input("Enter the digits: "))
s = 0
while(n!=0):
    r = n % 10
    s = s*10 + r
    n = n // 10
print("Reverse of the digits is: ", s)
