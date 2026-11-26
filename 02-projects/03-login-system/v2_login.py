#Login-System v2

def check_credentials(username, password):
    main_id = "admin"
    main_pass = "q1w2e3"
    if username != main_id and password != main_pass:
        return "both_wrong"
    elif username != main_id and password == main_pass:
        return "wrong_username"
    elif username == main_id and password != main_pass:
        return "wrong_password"
    else: 
        return "correct"

def get_credentials(prompt):
    return input(prompt).lower()

def login():
    move = 3
    while move > 0:
        username = get_credentials("Username: ")
        password = get_credentials("Password: ")
        result = check_credentials(username, password)
        if result == "both_wrong":
            print("The username and password are incorrect!")
            move -= 1
            print(f"You have {move} chances left!")
        elif result == "wrong_username":
            print("The username is incorrect!")
            move -= 1
            print(f"You have {move} chances left!")
        elif result == "wrong_password":
            print("The password is incorrect!")
            move -= 1
            print(f"You have {move} chances left!")
        else:
            print(f"Welcome, {username}")
            break
    else:
        print("Your account has been blocked! Please contact your administrator.")

def main():
    login()

if __name__ == "__main__": main()