from models.bank_fn.bank_data import accountNamesList, accountBalancesList, accountPasswordsList


def accountInfo(accountNumber) -> None:
    """
    display account informatiom by account number
    """
    global accountNamesList, accountBalancesList, accountPasswordsList
    accountNumber = int(accountNumber)
    print('Account', accountNumber)
    print('Name', accountNamesList[accountNumber])
    print('Balance:', accountBalancesList[accountNumber])
    print('Password:', accountPasswordsList[accountNumber])
    print()
