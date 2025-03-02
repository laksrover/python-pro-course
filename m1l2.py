import random
symbols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
pass_len = int(input("password length?"))
fin_pass = ""

for i in range(pass_len):
    fin_pass += symbols[random.randint(0,71)]
print(fin_pass)
