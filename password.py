# Features to add:
# 1. Password Analyzer
# 2. Generate Password
# 3. Save Password
# 4. Retrieve Password
# 5. Update Password
# 6. Exit 

# 1 Create the Menu, 
#how to store the passwords? How to retrieve them? Should I recommend a password in every feature(analyzer)? 
# 2 Create the Password Analyzer


print("------------------------------")
print ("Welcome to UrPass") #name of the app/web
print("------------------------------")


# Change everything to english "IMPORTANT"


import random
import string

passwords = {} # I think I dont need this anymore since I am using a txt file / Question to ask.

def menu():
    while True:
        print("Please select an option:\n")
        print("╔----------------------╗")
        print("| 1. Password Analyzer |")
        print("| 2. Generate Password |")
        print("| 3. Save Password     |")
        print("| 4. Retrieve Password |")
        print("| 5. Update Password   |")
        print("| 6. Exit              |")
        print("╚----------------------╝")

        choice = input()

        if choice == "1":
            password = input("Enter the password you want to analyze: ")
            password_analyzer(password)
        elif choice == "2":
            password = generate_password()
            print("Generated password:", password)
        elif choice == "3":
            app_web = input("Enter the name of the website/Storage: ")
            username = input("Enter the username: ") 
            password = input("Enter the password: ")
            save_password(app_web, username, password)
        elif choice == "4":
            app_web = input("Enter the name of the website/Storage: ")
            retrieve_password(app_web)
        elif choice == "5":
            app_web = input("Enter the name of the website/Storage: ")
            username = input("Enter the username: ") 
            password2 = input("Enter the new password: ")
            update_password(app_web, password2, username)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

# I'll be good if I remove the "username" variable from the function and just return the password


def password_analyzer(password):
    length = len(password)
    lowercase = False
    uppercase = False
    digit = False
    special_char = False

    for char in password:
        if char.islower():
            lowercase = True
        elif char.isupper():
            uppercase = True
        elif char.isdigit():
            digit = True
        elif char in "!@#$%^&*()_+-=[]{}|;':\",./<>?":
            special_char = True

    if length < 8:
        print("The password is very short. It is recommended to use at least 8 characters.")
        return False
    elif not lowercase:
        print("Must contain at least one lowercase letter.")
        return False
    elif not uppercase:
        print("Must contain at least one uppercase letter.")
        return False
    elif not digit:
        print("Must contain at least one number.")
        return False
    elif not special_char:
        print("Must contain at least one special character.")
        return False
    else:
        print("Password is strong.")
        return True


def generate_password():
    length = 12
    password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))
    while not password_analyzer(password):
        password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))
    return password


def save_password(app_web, username, password):
    if app_web in passwords:
        passwords[app_web][username] = password
    else:
        passwords[app_web] = {username: password}
    with open("passwords.txt", "a") as f:
        f.write(f"Password saved for {username} in {app_web}, {password}\n")
    print("Password saved successfully")


def retrieve_password(app_web):
    with open ('passwords.txt', 'rt') as myfile:  
        for myfile in myfile:  
         password = myfile.split(", ")[1].strip() 
         app_Web = myfile.split(", ")[0].strip()          
         if(app_web in app_Web):
             print("Your password is:", password)
             break
        else: 
            print("Password not found")
        

def update_password(app_web, username, password2):
    f = open("passwords.txt", 'r+')
    d = f.readlines()
    f.seek(0)
    for i in d:
        if app_web in i:
            i = i.replace(i, f"Password updated for {password2} in {app_web}, {username}\n")
        f.write(i)
    f.truncate()
    f.close()
    print("Password updated successfully")


menu()




