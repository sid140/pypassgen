import random
import logo
print(logo)
user_request =input("Please enter your desired password combination: ")
password_str = ["Alfa", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Golf", "Hotel", "India", "Juliett", "Kilo", "Lima", "Mike", "November", "Oscar", "Papa", "Quebec", "Romeo", "Sierra", "Tango", "Uniform", "Victor", "Whiskey", "X-ray", "Yankee", "Zulu"]
new_pass_check = password_str[0:27]
pass_ran = random.randint(2356,5678)

if user_request == "Alphanum":
    print(random.choice(password_str) + str(pass_ran) * 5)

elif user_request ==  "Num":
    print(str(random.randint(1000,9999)) + str(pass_ran) * 5 )


