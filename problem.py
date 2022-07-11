# print the amount of prime number
amount = 0
for num in range(2, 10):
    if all(num%i !=0 for i in range(2, num)):
        amount += 1
print(amount)



 