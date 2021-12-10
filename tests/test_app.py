from programs.app import app


# check that instance creation works 
# check that the balance is correct
# check that category labelling is correct
def test_app_class_creation():

    database = app(
        [{
        "user_input": 'create',
        "new_category": 'food',
        "user_input_int": 100,
        "deposit_desc": "",
        "withdraw_desc": "",
        "transfer_dest": "",
        "cat_selection": "",
        "user_exit": 'exit'
    }]
    )
    
    assert database['food'].get_balance() == 100

# check that withdraw works
def test_app_withdraw():
    
    database = app(
        [{
            "user_input": 'create',
            "new_category": 'food',
            "user_input_int": 100,
            "deposit_desc": "",
            "withdraw_desc": "",
            "transfer_dest": "",
            "cat_selection": "",
            "user_exit": ""
        },
        {
            "user_input": 'withdraw',
            "new_category": 'food',
            "user_input_int": 20,
            "deposit_desc": "",
            "withdraw_desc": 'lunch',
            "transfer_dest": "",
            "cat_selection": "",
            "user_exit": "exit"
        }
    ])
    assert database['food'].get_balance() == 80

# check that insufficient balance check works 
def test_app_insufficient_balance():
    
    database = app(
        [{
            "user_input": 'create',
            "new_category": 'food',
            "user_input_int": 100,
            "deposit_desc": "",
            "withdraw_desc": "",
            "transfer_dest": "",
            "cat_selection": "",
            "user_exit": ""
        },
        {
            "user_input": 'withdraw',#
            "new_category": '',
            "user_input_int": 100,#
            "deposit_desc": "",
            "withdraw_desc": 'scam', #
            "transfer_dest": "",
            "cat_selection": "",
            "user_exit": ""
        },
        {
            "user_input": 'withdraw',#
            "new_category": '',
            "user_input_int": 20, #
            "deposit_desc": "",
            "withdraw_desc": 'lunch', #
            "transfer_dest": "",
            "cat_selection": "",
            "user_exit": "exit" #
        }
    ])
    assert database['food'].get_balance() == 0

# check that creating multiple budgets work 
def test_app_multi_cats():
    database = app(
        [{
            "user_input": 'create',
            "new_category": 'food',
            "user_input_int": 100,
            "deposit_desc": "",
            "withdraw_desc": "",
            "transfer_dest": "",
            "cat_selection": "",
            "user_exit": ""
        },
        {
            "user_input": 'create',
            "new_category": 'travel',
            "user_input_int": 500,
            "deposit_desc": "",
            "withdraw_desc": "",
            "transfer_dest": "",
            "cat_selection": "",
            "user_exit": ""
        },
        {
            "user_input": 'create',
            "new_category": 'accommodation',
            "user_input_int": 500,
            "deposit_desc": "",
            "withdraw_desc": "",
            "transfer_dest": "",
            "cat_selection": "",
            "user_exit": "exit"
        }])

    # testing procedure
    results_list = []
    for item in database.keys():
        results_list.append(item)
    assert results_list == ['food', 'travel', 'accommodation']

# check that transfer works 
def test_app_transfer():
    database = app(
        [{
            "user_input": 'create',
            "new_category": 'food',
            "user_input_int": 100,
            "deposit_desc": "",
            "withdraw_desc": "",
            "transfer_dest": "",
            "cat_selection": "",
            "user_exit": ""
        },
        {
            "user_input": 'create',
            "new_category": 'travel',
            "user_input_int": 500,
            "deposit_desc": "",
            "withdraw_desc": "",
            "transfer_dest": "",
            "cat_selection": "",
            "user_exit": ""
        },
        {
            "user_input": 'transfer',
            "new_category": '',
            "user_input_int": 20,
            "deposit_desc": "",
            "withdraw_desc": "",
            "transfer_dest": "food",
            "cat_selection": "",
            "user_exit": "exit"
        }])  

    # testing procedure
    results_list = []
    for item in database:
        if database[item].get_balance() == 120 or database[item].get_balance() == 480:
            results_list.append(database[item].get_balance())
    assert results_list == [120, 480]
    
# check that balance works 
def test_app_balance():
    database = app(
        [{
            "user_input": 'create',
            "new_category": 'food',
            "user_input_int": 100,
            "deposit_desc": "",
            "withdraw_desc": "",
            "transfer_dest": "",
            "cat_selection": "",
            "user_exit": ""
        },
        {
            "user_input": 'create',
            "new_category": 'travel',
            "user_input_int": 500,
            "deposit_desc": "",
            "withdraw_desc": "",
            "transfer_dest": "",
            "cat_selection": "",
            "user_exit": ""
        },
        {
            "user_input": 'transfer',
            "new_category": '',
            "user_input_int": 20,
            "deposit_desc": "",
            "withdraw_desc": "",
            "transfer_dest": "food",
            "cat_selection": "",
            "user_exit": ""
        },
        {
            "user_input": 'change',#
            "new_category": 'travel',#
            "user_input_int": 30,#
            "deposit_desc": "",
            "withdraw_desc": "",
            "transfer_dest": "",
            "cat_selection": "food",#
            "user_exit": ""
        },
        {
            "user_input": 'deposit',#
            "new_category": '',
            "user_input_int": 33,#
            "deposit_desc": "",
            "withdraw_desc": "",
            "transfer_dest": "",
            "cat_selection": "",#
            "user_exit": ""
        },
        {
            "user_input": 'withdraw',#
            "new_category": '',
            "user_input_int": 153, #
            "deposit_desc": "",
            "withdraw_desc": "",
            "transfer_dest": "",
            "cat_selection": "",
            "user_exit": "exit"#
        }])  

    # testing procedure
    assert database['food'].get_balance() == 0

# check that statement file creation works 
# check that statement is produced in format
def test_file_creation():
    database = app(
        [{
            "user_input": 'create',
            "new_category": 'food',
            "user_input_int": 100,
            "deposit_desc": "",
            "withdraw_desc": "",
            "transfer_dest": "",
            "cat_selection": "",
            "user_exit": ""
        },
        {
            "user_input": 'create',#
            "new_category": 'travel',#
            "user_input_int": 500,#
            "deposit_desc": "",
            "withdraw_desc": "",
            "transfer_dest": "",
            "cat_selection": "",
            "user_exit": ""
        },
        {
            "user_input": 'transfer',#
            "new_category": '',
            "user_input_int": 20,#
            "deposit_desc": "",
            "withdraw_desc": "",
            "transfer_dest": "food",#
            "cat_selection": "",
            "user_exit": ""
        },
        {
            "user_input": 'statement',#
            "new_category": '',
            "user_input_int": 0,#
            "deposit_desc": "",
            "withdraw_desc": "",
            "transfer_dest": "",
            "cat_selection": "",
            "user_exit": "exit"#
        }])  

    # testing procedure
    database['travel'].print_budget()

    with open(f"outputs/travel.txt", "r") as file:
        lines_actual = file.readlines()
    
    with open("outputs/travel_test.txt", "r") as file:
        lines_ref = file.readlines()

    assert lines_ref == lines_actual
    
# check that changing active category works

# check that exit command works 

'''further down the line we could have looked at more complex tests'''

