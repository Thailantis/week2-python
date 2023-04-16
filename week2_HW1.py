# Cube Number Test... Print out all cubed numbers up to the total value 1000. Meaning that if the cubed number is over 1000 break the loop.

i = 1
while True:
    cubed = i ** 3
    if cubed > 1000:
        break
    print(cubed)
    i += 1
    
# Get first prime numbers to 100
def prime_num(n):
    if n < 2:
        return False
    for n in range(1, 101, 2):
        if prime_num(n):
            print(prime_num)
          
 # Take in a users input for their age, if they are younger than 18 print kids, if they're 18 to 65 print adults, else print seniors
 age = int(input("Enter your age: "))
    if age < 18:
        print('kids')
    elif <= 65:
        print('adults')
    else:
        print('seniors')
