# GTST Company Login System
users = {
    "Nathan": "2313",
    "Geez": "pass231",
    "Abebe": "092313133",
    "Miki": "pl3s34D0n'tH4ckM3"
}

for attempt in range(5):

    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in users:
        if users[username] == password:
            print("Welcome to GTST Company!")
            break
        else:
            print("Incorrect Login!")
    else:
        print("Incorrect Login!")

else:
    print("Sorry u are limited!")
