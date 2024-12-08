import random
password="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
length=input("Напиши длину пароля - ")
password_real=""
for i in range(int(length)):
    password_real+=random.choice(password)
print(password_real)
