#ata

#example summision of 2 numbers
#def add (x,y)
#z = x+y
#return z
#print(9,8)


def prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


num = int(input("enter a number: "))
if prime(num):
    print("it is a prime number")
else:
    print("not a prime number")