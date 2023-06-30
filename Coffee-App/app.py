import database

MENU_PROMPT = """ ---- Coffeee Bean App ----

Please choose one of these options

1) add a new bean
2) see all beans
3) find a bean by name
4) see which preparation is best for a bean
5) exit

Your Selection: 

"""

def menu():
    connection = database.connect()
    database.create_tables(connection)

    while(user_input := input(MENU_PROMPT)) != 5:  # ha! walrus operator
        if user_input == "1":
            name = input("Entre name : ")
            method = input("Entre how you've prepared it : ")
            rating = int(input("what's your rating score (0-10) : "))

            database.add_bean(connection,name,method,rating)
            
        elif user_input == "2":
            beans = database.get_all_beans(connection)

            for bean in beans:
                print(bean)

        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        elif user_input =="5":
            pass
        else:
          print("invalid input please try again")

menu()