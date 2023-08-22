from models.bank_fn.bank_data import accountNamesList, accountBalancesList, accountPasswordsList


def newAccount(name, balance, password) -> None:
    """
    to create accounts with 3 fields
    """
    global accountNamesList, accountBalancesList, accountPasswordsList
    accountNamesList.append(name)
    accountBalancesList.append(balance)
    accountPasswordsList.append(password)
    print(f"{name}'s account is account number:", len(accountNamesList))
