import random

account_holders = {}


def init():

    selected_option = False

    while selected_option == False:
        print('welcome to our system')


        print('do you have an account with us?? ')
        print('Enter 1 if you have an account with us')
        print('Enter 2 if you want to register a new account')
        check_status = int (input())

        if check_status == 1:
            selected_option == True

            login()

        elif check_status == 2:
            selected_option == True

            create_account()

        else:
            print('You have selected an invalid option')


def account_no_generator():
    print('This is your account number ')

    return random.randrange(1111111111, 9999999999)

def create_account():
    print(' To create an account kiindly put in the requested details ')

    email = input(' Email:  ')
    first_name = input(' First Name:  ')
    last_name = input(' Last Name: ')
    password = input(' Password:  ')
    account_bal = int (input('Enter the amount to open your account '))

    if account_bal > 0:
        account_bal = account_bal
    
    else: 
        account_bal = 0

    account_no = account_no_generator()

    account_holders[account_no] = [email, first_name, last_name, password, account_bal]

    print(' your account has been created')
    print(f" Your account number is: {account_no} ")

    continue_session = False

    while continue_session == False:
        print('Do you Want To Login To Your account???')
        print('Press 1 to continue and Press 2 to end')
        continue_option =  int (input())

        if continue_option == 1:
            continue_session == True
            login()

        elif continue_option ==2:
            continue_session == True

            print('Thanks For Using Our Service!!!!!')

            exit()

        else:
            
            print(' You Selected an invalid option please try again ')



def login():


    print('**********************Welcome to the login page********************')

    successful_login = False

    while successful_login == False:

        account_no_given = int (input('Enter Your Account Number'))
        password_given = input('Enter Your Password')

        for account_no,userdetails in account_holders.items():
            if account_no == account_no_given:
                if password_given == userdetails[3]:
                    successful_login == True
                    print('Login Successful')
                    bankoperations(userdetails)
            
            else:
                
                print('Invalid Username and password')



def bankoperations(user):
    print(f'Welcome {user[1]}, {user[2]}  ')
  

    valid_operation = False

    while valid_operation == False:
        print('What would you like to do :')
        print('Enter 1 to withdraw, Enter 2 to deposit, Enter 3 to Logout, Enter 4 to exit')

        selected_operation = int(input() )

        if selected_operation == 1:
            valid_operation == True
            user[4] = withdraw(user[4])
            bankoperations(user)

        elif selected_operation == 2:
            valid_operation == True
            user[4] = deposit(user[4])
            bankoperations(user)

        elif selected_operation == 3:
            valid_operation == True
            login()

        elif selected_operation == 4:
            valid_operation == True
            exit()

        else:
            
            print('Invalid Option Selected Please Try Again')

        

def withdraw(acc_bal):
    

    is_amount_withdrawable = False

    while is_amount_withdrawable == False:
        withdraw_amount= int (input('How much will You like To Withdraw'))

        if withdraw_amount < acc_bal:
            is_amount_withdrawable == True
            acc_bal = acc_bal-withdraw_amount


            print('Transaction Completed')
            return acc_bal
            

        else:
            print('Insufficient Funds Try again')




def deposit(acc_bal):
    
    deposit_amount = int (input('How Much Would YOu Like to Deposit'))

    acc_bal = acc_bal + deposit_amount
    print('Transaction Completed')

    return acc_bal


init()

    







