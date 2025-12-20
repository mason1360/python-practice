# check password strength based on length

password = input("Enter password: ")

if len(password) < 8:
    print("Weak password (minimum 8 characters)")
else:
    print("Strong password")
