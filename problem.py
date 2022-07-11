# print the amount of prime number
amount = 0
# for num in range(2, 1000):
#     if all(num%i !=0 for i in range(2, num)):
#         amount += 1
# print(amount)

# for num in range(2, 100):
#     for i in range(2, num):
#         if(num%i != 0):
#             break
#     else:
#         print(num)
#         amount += 1
# print(amount)
prime = True
for num in range(100, 201):
    for i in range(2, num):
        if(num%i == 0):
            prime = False
            break

    if(prime):
        print(num)
        amount += 1
    prime = True
print(amount)

 