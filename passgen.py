import random
import logo
print(logo)
user_request =input("Please enter your desired password combination: ")
password_int = random.randint(1000,9999)
password_str = ["Alfa", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Golf", "Hotel", "India", "Juliett", "Kilo", "Lima", "Mike", "November", "Oscar", "Papa", "Quebec", "Romeo", "Sierra", "Tango", "Uniform", "Victor", "Whiskey", "X-ray", "Yankee", "Zulu"]
new_pass_check = password_str[0:27]


if user_request == "Alphanum":
    print(random.choice(password_str) + str(password_int))

elif user_request == "alpha":
    print(password_int + new_pass_check)
