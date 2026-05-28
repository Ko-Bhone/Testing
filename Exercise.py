num = int(input("Enter your Number:"))

is_prime = True

if num < 1:
    is_prime = False

for i in range(2,num):
    if num % i == 0:
        is_prime = True
        break


if is_prime:
    print("Prime")
else:
    print("Not Prime")