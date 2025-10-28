Users = {
    "user1": "P@ss",
    "user2": "w0rd",
    "user3": "bgl_11"
}

def register(username):
    if username in Users:
        print(f"{username} already exist")
        login()
    else:
        password = input("Enter Password: ")
        Users[username] = password
        print("New User registered Successfully")
def login():
    while True:
        username = input("Enter Username: ")
        if username not in Users:
            print(f"new user {username} detected")
            new_user = input("Need new Registration? ")
            if new_user == "yes" or new_user == "y":
                register(username)
            else:
                continue
        password = input("Enter Password: ")
        if Users[username] == password:
            print(f"Hello, {username}")
            print(f"{len(Users)} users registered so far")
            break
        else:
            print("Invalid Credentials. \n Try again!")
login()
print(Users)