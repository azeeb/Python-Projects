import random
import math

alpha = 'abcdefghijklmnopqrstuvwxyz'
num = '0123456789'
special = "@#$%&*"

#user input
pass_len = int(input("Please enter the length of the password you wanna generate: "))

alpha_len = pass_len//2
num_len = math.ceil(pass_len*30/100)
special_len = pass_len - alpha_len - num_len

password = []

def gen_pwd(length, array, is_alpha = False):
    for i in range(length):
        index = random.randint(0, len(array)-1)
        character = array[index]
        if is_alpha == 1:
            case = random.randint(0,1)
            if case == 1:
                character = character.upper()
        password.append(character)

#creating alphabets
gen_pwd(alpha_len, alpha, True)
#numeric password
gen_pwd(num_len, num)
#special passwrod
gen_pwd(special_len, special)
#shuffle and generate password list
random.shuffle(password)

gen_password = ""

#convert list to string
for i in password:
    gen_password = gen_password + str(i)
print(gen_password)