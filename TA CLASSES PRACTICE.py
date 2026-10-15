def add(x, y):
    return x + y

print(add(9, 8))


def prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


num = int(input("ENTER A NUMBER: "))
if prime(num):
    print(f"{num} is a prime number")
else:
    print("NOT A PRIME NUMBER")
