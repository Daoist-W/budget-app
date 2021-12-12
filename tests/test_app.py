from programs.app import app
from programs.user_input import user_inputs


# check that instance creation works 
# check that the balance is correct
# check that category labelling is correct
# check that exit command works 
def test_app_class_creation():
    database = app(
        [user_inputs(
            USER_INPUT="create",
            NEW_CAT="food", 
            USER_INPUT_INT="100", 
            USER_EXIT="exit")]
    )
    
    assert database['food'].get_balance() == 100

# check that withdraw works
def test_app_withdraw():
    database = app(
        [user_inputs(
            USER_INPUT="create",
            NEW_CAT="food", 
            USER_INPUT_INT="100"),
        user_inputs(
            USER_INPUT="withdraw",
            USER_INPUT_INT="20",
            WITHDRAW_DESC="lunch", 
            USER_EXIT="exit")       
    ])
    assert database['food'].get_balance() == 80

# check that insufficient balance check works 
def test_app_insufficient_balance():
    database = app([
        user_inputs(
            USER_INPUT="create",
            NEW_CAT="food", 
            USER_INPUT_INT="100"),
        user_inputs(
            USER_INPUT="withdraw",
            USER_INPUT_INT="100",
            WITHDRAW_DESC="lunch"),
        user_inputs(
            USER_INPUT="withdraw",
            USER_INPUT_INT="20",
            WITHDRAW_DESC="lunch", 
            USER_EXIT="exit")
    ])
    assert database['food'].get_balance() == 0

# check that creating multiple budgets work 
def test_app_multi_cats():
    database = app([
        user_inputs(
            USER_INPUT="create",
            NEW_CAT="food", 
            USER_INPUT_INT="100"),
        user_inputs(
            USER_INPUT="create",
            NEW_CAT="travel",
            USER_INPUT_INT=500),
        user_inputs(
            USER_INPUT="create",
            NEW_CAT="accommodation",
            USER_INPUT_INT=500,
            USER_EXIT="exit")
    ])

    # testing procedure
    results_list = []
    for item in database.keys():
        results_list.append(item)
    assert results_list == ['food', 'travel', 'accommodation']

# check that transfer works 
def test_app_transfer():
    database = app([
        user_inputs(
            USER_INPUT="create",
            NEW_CAT="food", 
            USER_INPUT_INT="100"),
        user_inputs(
            USER_INPUT="create",
            NEW_CAT="travel",
            USER_INPUT_INT=500),
        user_inputs(
            USER_INPUT="transfer",
            USER_INPUT_INT=20,
            TRANSER_DEST="food", 
            USER_EXIT="exit")
    ])  

    # testing procedure
    results_list = []
    for item in database:
        if database[item].get_balance() == 120 or database[item].get_balance() == 480:
            results_list.append(database[item].get_balance())
    assert results_list == [120, 480]
    
# check that balance works 
# check that changing active category works
def test_app_balance():
    database = app([
        user_inputs(
            USER_INPUT="create",
            NEW_CAT="food", 
            USER_INPUT_INT="100"),
        user_inputs(
            USER_INPUT="create",
            NEW_CAT="travel",
            USER_INPUT_INT=500),
        user_inputs(
            USER_INPUT="transfer",
            USER_INPUT_INT=20,
            TRANSER_DEST="food"),
        user_inputs(
            USER_INPUT="change",
            CAT_SELECTION="food"),
        user_inputs(
            USER_INPUT="deposit",
            USER_INPUT_INT=33,
            DEPOSIT_DESC="test"),
        user_inputs(
            USER_INPUT="withdraw",
            USER_INPUT_INT=153,
            DEPOSIT_DESC="damn daniel", 
            USER_EXIT="exit")
    ])  

    # testing procedure
    assert database['food'].get_balance() == 0

# check that statement file creation works 
# check that statement is produced in format
def test_file_creation():
    database = app([
        user_inputs(
            USER_INPUT="create",
            NEW_CAT="food", 
            USER_INPUT_INT="100"),
        user_inputs(
            USER_INPUT="create",
            NEW_CAT="travel",
            USER_INPUT_INT=500),
        user_inputs(
            USER_INPUT="transfer",
            USER_INPUT_INT=20,
            TRANSER_DEST="food"),
        user_inputs(
            USER_INPUT="statement", 
            USER_EXIT="exit")
    ])  

    # testing procedure
    database['travel'].print_budget()

    with open(f"programs/outputs/travel.txt", "r") as file:
        lines_actual = file.readlines()
    
    with open("programs/outputs/travel_test.txt", "r") as file:
        lines_ref = file.readlines()

    assert lines_ref == lines_actual
    

'''further down the line we could have looked at more complex tests'''

