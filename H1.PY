# CLASS WORK
users = ['Nathan', '2313', 'Geez', 'pass231',
         'Abebe', '092313133', 'Miki', 'pl3s34D0ntH4ckM3!']

usernames = users[0::2]
passwords = users[1::2]


print(" usernames are:", usernames)
print(" passwords are:", passwords)

# HOMEWORK
users = {
    'Nathan': '2313',
    'Geez': 'pass231',
    'Abebe': '092313133',
    'Miki': 'pl3s34D0ntH4ckM3!'
}

username = input("Enter username: ")

print("Password:", users[username])
