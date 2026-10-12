def validate_amount(amount):
    if amount <= 0:
        raise ValueError("amount must be positive")


def create_account(owner, balance=0.0):
    return {"owner": owner, "balance": balance}


def deposit(account, amount):
    validate_amount(amount)
    return {**account, "balance": account["balance"] + amount}


def withdraw(account, amount):
    validate_amount(amount)
    if amount > account["balance"]:
        raise ValueError("insufficient funds")
    return {**account, "balance": account["balance"] - amount}


def show(account):
    return f"{account['owner']}: {account['balance']:.2f}"


if __name__ == "__main__":
    acct = create_account("Aisha", 100.0)
    acct = deposit(acct, 50.0)
    acct = withdraw(acct, 30.0)
    print(show(acct))   # Aisha: 120.00

