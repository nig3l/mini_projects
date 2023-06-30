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
                print(f"{bean[1]} ({bean[2]}) - {bean[3]}/10")

        elif user_input == "3":
            name = input("Entre bean name to find: ")
            beans = database.get_all_beans_by_name(connection,name)

            for bean in beans:
                print(f"{bean[1]} ({bean[2]}) - {bean[3]}/10")

        elif user_input == "4":
            name = input("entre bean name to find : ")
            best_method = database.get_best_preparation_for_bean(connection,name)

            print(f"The best preparation for {name} is : {best_method[2]}")


        elif user_input =="5":
            pass
        else:
          print("invalid input please try again")

menu()