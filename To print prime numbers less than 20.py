#To print prime numbers less than 20.
a=20
print("The Prime Numbers are: ")
for i in range(2,a+1):
    prime=True
    for j in range(2, int(i**0.5)+1):
        if i%j==0:
            prime=False
            break
    if prime:
        print(i, end=" ")
