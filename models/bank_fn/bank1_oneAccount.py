# Non-OOP
# Bank Version 1
# Single account

test_data = [{
    'accountName': 'Joe',
    'accountBalance': 100,
    'accountPassword': 'soup',
}]


while True:
    print()
    print('Press b to get the balance')
    print('Press d to make a deposit')
    print('Press w to make a withdrawal')
    print('Press s to show the account')
    print('Press q to quit')
    print()

    action = input('What do you want to do? ')
    action = action.lower()  # force lowercase
    action = action[0]  # just use first letter
    print()

    if action == 'b':
        print('Get Balance:')
        userPassword = input('Please enter the password: ')
        if userPassword != test_data[0].get('accountPassword'):
            print('Incorrect password')
        else:
            print('Your balance is:', test_data[0].get('accountBalance'))
    elif action == 'd':
        print('Deposit:')
        userDepositAmount = input('Please enter amount to deposit: ')
        userDepositAmount = int(userDepositAmount)
        userPassword = input('Please enter the password: ')
        if userDepositAmount < 0:
            print('You cannot deposit a negative amount!')
        elif userPassword != test_data[0].get('accountPassword'):
            print('Incorrect password')
        else:  # OK
            test_data[0]['accountBalance'] += userDepositAmount
            print('Your new balance is:', test_data[0].get('accountBalance'))
    elif action == 's':  # show
        print('Show:')
        print(' Name', test_data[0].get('accountName'))
        print(' Balance:', test_data[0].get('accountBalance'))
        print(' Password:', test_data[0].get('accountPassword'))
        print()
    elif action == 'q':
        break
    elif action == 'w':
        print('Withdraw:')
        userWithdrawAmount = input('Please enter the amount to withdraw: ')
        userWithdrawAmount = int(userWithdrawAmount)
        userPassword = input('Please enter the password: ')
        if userWithdrawAmount < 0:
            print('You cannot withdraw a negative amount')
        elif userPassword != test_data[0].get('accountPassword'):
            print('Incorrect password for this account')
        elif userWithdrawAmount > test_data[0].get('accountBalance'):
            print('You cannot withdraw more than you have in your account')
        else:  # OK
            test_data[0]['accountBalance'] -= userWithdrawAmount
            print('Your new balance is:', test_data[0].get('accountBalance'))
print('Done')
