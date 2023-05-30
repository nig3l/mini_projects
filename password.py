import getpass

database = {"chief.schwab":"46573","hillaery.monet":"097543"}

username = input("Entre your username : ")
password = getpass.getpass("entre your password : ")

for i in database.keys():
    if username == i:
        while password != database.get(i):
            password = getpass.getpass("do it again : ")
            

        print("verified")
