import budget


def app (list_of_commands=None):
    
    # input management for testing purposes
    if list_of_commands is not None:
        command_index = 0
        user_input = list_of_commands[command_index]["user_input"]
        new_category = list_of_commands[command_index]["new_category"]
        user_input_int = int(list_of_commands[command_index]["user_input_int"])
        deposit_desc = list_of_commands[command_index]["deposit_desc"]
        withdraw_desc = list_of_commands[command_index]["withdraw_desc"]
        transfer_dest = list_of_commands[command_index]["transfer_dest"]
        cat_selection = list_of_commands[command_index]["cat_selection"]
        user_exit = list_of_commands[command_index]["user_exit"]

    # need to set trigger regardless of manual / auto test state
    trigger = False

    # create loop control and dictionary to store object states
    # also variables for back end of logic control
    loop = True
    database = dict()
    active_category = None
    list_of_valid_inputs = [
        'create',
        'deposit',
        'withdraw',
        'transfer',
        'balance',
        'statement',
        'change',
        'exit'
    ]

    # this loop of code will continue to ask for instruction until
    # cancelled or user types "exit" into terminal when prompted
    # where list_of_commands is shown
    while loop == True:
        # updating pytest inputs
        if trigger == True:
            print(command_index)
            user_input = list_of_commands[command_index]["user_input"]
            new_category = list_of_commands[command_index]["new_category"]
            user_input_int = int(list_of_commands[command_index]["user_input_int"])
            deposit_desc = list_of_commands[command_index]["deposit_desc"]
            withdraw_desc = list_of_commands[command_index]["withdraw_desc"]
            transfer_dest = list_of_commands[command_index]["transfer_dest"]
            cat_selection = list_of_commands[command_index]["cat_selection"]
            user_exit = list_of_commands[command_index]["user_exit"]
            command_index += 1

        # user prompt for instructions
        if active_category:
            print(f"Active account: {active_category}")

        if list_of_commands is None:
            user_input = input(
                "What would you like to do? \n" +
                "(create, deposit, withdraw, transfer, balance, statement, change, exit): "
            )

        # core command logic  
        if user_input not in list_of_valid_inputs:
            print("Invalid command, please try again ...")

        elif user_input == "create":

            try:
                if list_of_commands is None:
                    user_input_int = int(input("Please enter initial amount: "))
                    new_category = input("Please name budget category: ")
                active_category = new_category
                print(user_input_int)
                database[new_category] = budget.Category(new_category, user_input_int)
                print("success")
            except:
                print("Incorrect create input, please start again") 

        elif user_input == "deposit":
            try:
                if list_of_commands is None:
                    user_input_int = int(input("Please enter deposit amount: "))
                    deposit_desc = input("Please enter description: ")
                database[active_category].deposit(user_input_int, deposit_desc)
            except:
                print("Incorrect deposit input, please start again") 

        elif user_input == "withdraw":
            try:
                if list_of_commands is None:
                    user_input_int = int(input("Please enter withdraw amount: "))
                    withdraw_desc = input("Please enter description: ")
                database[active_category].withdraw(user_input_int, withdraw_desc)
            except:
                print("Incorrect withdraw input, please start again") 

        elif user_input == "transfer":
            try:
                if list_of_commands is None:
                    user_input_int = int(input("Please enter transfer amount: "))
            
                # creating a string formatted list for user review
                list_of_categories = "List: \n"
                for key, value in database.items():
                    list_of_categories += key + "\n"

                # obtaining user input, this needs to be constrained
                if list_of_commands is None:
                    transfer_dest = input(
                        "Which category are you tranferring to?: \n" +
                        f"{list_of_categories}"
                    )
                
                # commands to transfer money between accounts 
                database[active_category].transfer(user_input_int, database[transfer_dest])

            except:
                print("Incorrect transfer input, please start again") 

        elif user_input == "balance":
            try:
                print(f"Current balance: {database[active_category].get_balance()}")
            except:
                print("Something went wrong with the balance request, please start again") 
                        
        elif user_input == "statement":
            # try:
                for line in database[active_category].print_budget():
                    print(line)
            # except:
                print("Incorrect balance input, please start again") 
        
        elif user_input == "change":

            # creating a string formatted list for user review
            cat_list = []
            for key, value in database.items():
                cat_list.append(key)

            if list_of_commands is None:
                cat_selection = input(
                        "Choose an available category: \n" +
                        f"{cat_list} \n"
                    )
            if cat_selection in cat_list:
                active_category = cat_selection
            else:
                print("Incorrect change input, please start again")
        
        # command for initiating update of input variables during testing
        if list_of_commands is not None:
            trigger = True
            # testing command for quitting during testing
            if user_exit == "exit":
                user_input = user_exit

        # check to exit program
        if user_input == "exit":
            loop = False
            print("Exiting ...")
    return database

# should be commented out unless manual testing
app ()