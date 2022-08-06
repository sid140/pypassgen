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
system_chose = random.choice(sym_now)
encrypt = str(new_pass_check[3]) + str(sym_now)
if user_request == "Alphanum":
    print(random.choice(password_str) + encrypt * 2)
    input()
elif user_request ==  "Num":
    print(str(random.randint(1000,9999)) + str(system_chose) * 5 )
    input()

