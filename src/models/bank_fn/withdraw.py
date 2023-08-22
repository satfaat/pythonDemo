def withdraw(amountToWithdraw, password):
    global accountName, accountBalance, accountPassword
    if amountToWithdraw < 0:
        print('You cannot withdraw a negative amount')
        return None

    if password != accountPassword:
        print('Incorrect password for this account')
        return None

    if amountToWithdraw > accountBalance:
        print('You cannot withdraw more than you have in your account')
        return None
    accountBalance -= amountToWithdraw
    return accountBalance
