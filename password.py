# Features to add:
# 1. login and register(working on it)

# print image in console ? 


import pyfiglet
text = pyfiglet.figlet_format("UrPass",
                              font = "epic")


print("------------------------------")
print ("-------- Welcome to ---------")
print(text) #name of the app/web
print("This is a password manager where you can store your passwords and usernames")
print("------------------------------")




import random
import string
import colorama
import traceback

passwords = {} # ?

def menu(): #this is the menu inside the app.
    
    
    while True:
        try:
            print(colorama.Fore.BLUE + "Please select an option:\n")
            print("╔----------------------╗")
            print("| 1. Password Analyzer |")
            print("| 2. Generate Password |")
            print("| 3. Save Password     |")
            print("| 4. Retrieve Password |")
            print("| 5. Update Password   |")
            print("| 6. Exit              |")
            print("╚----------------------╝\n")
            print("Option: ")

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
                print(colorama.Fore.YELLOW +"Goodbye!")
                break
            else: 
                print(colorama.Fore.RED + "Invalid option. Please try again.")
                raise ValueError("Invalid option")
            
        except ValueError as ve:
            with open("error.log", "a") as f:
                 f.write("Unexpected error: {}\n".format(str(ve)))
                 print(colorama.Fore.RED + "Invalid option. Please try again.")
        
        except:
            traceback.print_exc()


def password_analyzer(password):

    length = len(password)
    lowercase = False
    uppercase = False
    digit = False
    special_char = False
    missing_criteria = []

    for char in password:
        if char.islower():
            lowercase = True
        elif char.isupper():
            uppercase = True
        elif char.isdigit():
            digit = True
        elif char in "!@#$%^&*()_+-=[]{}|;':\",./<>?":
            special_char = True

    if length < 12:
        missing_criteria.append("The password is very short. It is recommended to use at least 8 characters.")
    if not lowercase:
        missing_criteria.append("Must contain at least one lowercase letter.")
    if not uppercase:
        missing_criteria.append("Must contain at least one uppercase letter.")
    if not digit:
        missing_criteria.append("Must contain at least one number.")
    if not special_char:
        missing_criteria.append("Must contain at least one special character.")
        
    if missing_criteria:
        print(colorama.Fore.RED + "Password is not strong. The following criteria are missing:")
        for criterion in missing_criteria:
            print("- " + criterion)
        return False
    else:
        print(colorama.Fore.GREEN +"Password is strong.")
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
    print(colorama.Fore.GREEN +"Password saved successfully")



def retrieve_password(app_web):
    with open ('passwords.txt', 'rt') as myfile: 
        try: 
            for myfile in myfile:  
                password = myfile.split(", ")[1].strip() 
            app_Web = myfile.split(", ")[0].strip()          
            if(app_web in app_Web):
                print("Your password is:", password)
            else: 
                print(colorama.Fore.RED + "Password not found")
                raise ValueError("Invalid option")
            
        except ValueError as ve:
            with open("error.log", "a") as f:
                 f.write("Unexpected error, Username or Password: {}\n".format(str(ve)))
                 print(colorama.Fore.RED + "Invalid Username or Password. Please try again.")
        
        except:
            traceback.print_exc()
        


def update_password(app_web, username, password2):
    f = open("passwords.txt", 'r+')
    d = f.readlines()
    f.seek(0)
    try: 
        for i in d:
            if app_web in i:
                i = i.replace(i, f"Password updated for {password2} in {app_web}, {username}\n")
            f.write(i)
        f.truncate()
        f.close()
        print(colorama.Fore.GREEN + "Password updated successfully")
    except ValueError as ve:
        with open("error.log", "a") as f:
             f.write("Unexpected error, Username or Password: {}\n".format(str(ve)))
             print(colorama.Fore.RED + "Invalid Username or Password. Please try again.")
    except:
        traceback.print_exc()



menu()




#hot to test my code?
#how to make the code more efficient? less lines of code? 
#how to make the code more secure? 
#how to make the code more user friendly? Perhaps I need more FE (Front End)
#how to make the code more professional?
#how to make the code more readable?



