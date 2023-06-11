import getpass

database = {"chief.schwab":"46573","hillaery.monet":"097543"}

username = input("Entre your username : ")
password = getpass.getpass("entre your password : ")

for i in database.keys():
    if username == i:
        while password != database.get(i):
            password = getpass.getpass("do it again : ")
            

        print("verified")

        
#-- version

'''import getpass

users = {"chief.schwab": "46573", "hillaery.monet": "097543"}

username = input("Enter your username: ")
password = getpass.getpass("Enter your password: ")


# if username not in users:
#     print("ooops something went wrong")

try:
    if username in users and users[username] == password:
        print("Verified")
    else :
        print("try again")

except KeyError:
    print("Invalid username or password")

'''
