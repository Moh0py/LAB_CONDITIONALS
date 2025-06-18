name = input("Enter Your Name: ")
email = input("Enter Your Email: ")

if len(name) > 2:
    if email.endswith("@gmail.com"):
        print(f"Welcome {name}, you registered with the email {email}!")
    else:
        print("The email is not valid, please provide a valid email.")
else:
    print("The name length must be more than 2 characters, please provide a valid name.")
