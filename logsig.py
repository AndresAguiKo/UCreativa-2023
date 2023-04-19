def home(option=None):
    option = input("Login | Signup | Exit: ")
    if option == "Login":
        login()
    elif option == "Signup":
        register()
    elif option == "Exit":
        print("Goodbye")


def register():
    db = open('logsig.txt', 'r+')
    username = input("Create your username: ")
    password = input("Create your password: ")
    password2 = input("Confirm your password: ")
    u = []
    p = []
    for i in db:
        a, b = i.split(",")
        b = b.strip()
        u.append(a)
        p.append(b)
    data = dict(zip(u, p))
    db.close()

    if password != password2:
        print("Passwords don't ,atch, restart")
        register()
    else:
        if len(password)<=4:
            print("Password must be at least 4 characters long")
            register()
        elif username in u:
            print("Username already taken")
            register()
        else:
            db = open('logsig.txt', 'a')
            db.write(username + " , " + password+"\n")
            db.close()
            print("Registration successful, Welcome to UrPass " + username + "!!")
            print("You can now login")


def login():
    db = open('logsig.txt', 'r')
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    u = []
    p = []
    for i in db:
        a, b = i.split(", ")
        b = b.strip()
        u.append(a)
        p.append(b)
    data = dict(zip(u, p))
    db.close()

    if username not in a:
        print("Username not found")
        login()
    elif password != b:
        print("Incorrect password")
        login()
    else:
        print("Login successful, Welcome to UrPass " + username + "!!")


home()

    
