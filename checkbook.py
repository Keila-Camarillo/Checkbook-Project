# read file and return the current balance
import os.path

def get_balance():
    '''Read the current balance'''
    if os.path.isfile('tran_history.txt'):
        with open('tran_history.txt', 'r') as cb:
            return cb.readlines()[-1].split(',')[1]
    else:
        return '0.0'

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def record_transaction(isDebit=0):
    '''
        Record debit/credit transactions 
    '''
    current_balance = float(get_balance())

    while True:
        user_input = input('Please enter amount: $')
        if isfloat(user_input):
            break
        print("Invalid response")

    trans_input= round((float(user_input),-float(user_input))[isDebit],2)
    str_trans = str(trans_input)

    new_balance = current_balance + trans_input
    with open('tran_history.txt', 'a+') as cb:
        cb.write("\n" + str_trans + ',' + str(new_balance))
    print("You succesfully "+("deposited","withdrew")[isDebit]+': $ ' + str_trans + "\nNew balance: $" + str(new_balance))

def exit():
    '''exit program'''
    print('Thank you! Goodbye')
    quit()

print('''~~~ Welcome to your terminal checkbook! ~~~''')

while True:
    print('''
    What would you like to do?

    1) view current balance
    2) record a debit (withdraw)
    3) record a credit (deposit)
    4) exit''')

    user_input = input('Your choice: ' )
    if user_input == '1':
            print('New balance: $' + get_balance())
    elif user_input == '2':
        record_transaction(1)
    elif user_input == '3':
        record_transaction()
    elif user_input == '4':
        exit()
    else:
        print('Invalid response. Try again. Please select an option from 1 - 4' )
