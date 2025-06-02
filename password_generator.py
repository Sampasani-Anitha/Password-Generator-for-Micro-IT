import random
print("Welcome to the PyPassword Generator!")

letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
symbols = ['!','@','#','$','%','^','&','*','(',')','~','_','-','?','+']
numbers = ['0','1','2','3','4','5','6','7','8','9']

pass_letters = int(input("How many letters would you like in the password?\n"))
pass_symbols = int(input("How many Symbols would you like in the password?\n"))
pass_num = int(input("How many Numbers would you like in the password?\n"))

password = []
for i in range(1,pass_letters+1):
    password += random.choice(letters)
for i in range(1, pass_symbols + 1):
    password += random.choice(symbols)
for i in range(1, pass_num + 1):
    password += random.choice(numbers)

random.shuffle(password)
pw = ""
for i in password:
    pw += i
print(f"Your Password is : {pw}")