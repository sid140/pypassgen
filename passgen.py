import random
import logo
import Readme
print(logo)
print("Passgen")
user_request =input("Please enter your desired password combination: ")
password_str = ["Alfa", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Golf", "Hotel", "India", "Juliett", "Kilo", "Lima", "Mike", "November", "Oscar", "Papa", "Quebec", "Romeo", "Sierra", "Tango", "Uniform", "Victor", "Whiskey", "X-ray", "Yankee", "Zulu"]
new_pass_check = password_str[0:27]
pass_ran = random.randint(2356,5678)
sym_now = "!@#$%^&*()"
sym_now_len = len(sym_now)
system_chose = random.choice(sym_now)
encrypt = str(new_pass_check[3]) + random.choice(str(sym_now) * 5)
encode = input("Input custom characters: ")
double_encrypt = str(encrypt + encode)
new_pass_check_2 = len(double_encrypt)

def passw(encode):
    if user_request == "KEYGUESS".lower():
        computer_request = input("Do you need extra  chars to be add(Y/N):? ")
        if computer_request == "Y":
            print(str(random.choice(password_str) + str(double_encrypt)))
        input()
    elif computer_request == "N":
        print("Exiting")

passw(f"encode")