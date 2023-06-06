'''Password Strength Checker'''
#Enter the password
#It should be morethan 8 characters 
#mixed of strings and numbers

import re
import string
import random

password = input(f"Enter your password here  : ")
generated_password = 8
res = ''.join(random.choices(string.ascii_uppercase +string.ascii_lowercase+
                             string.digits, k=generated_password))


len_th = len(password)
print(f"\nYour password have {len_th} characters")


if len_th >= 8:
    if re.search("[A-Z]",password):

        if re.search("[a-z]",password):
            
            if re.search("[0-9]",password):

                print("Password is strong")
            else:

                print("Password must contain a Number")
        else :

            print('Password must contain a Small letter')
    else :

        print("Password must contain a Capital Letter")
else:
    print("\nPassword is weak")
    print("\nTry this password instead  : " + str(res))
    print("\n")



    

