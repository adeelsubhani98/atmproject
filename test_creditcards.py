from atmproject.bankcard import BankCard
from atmproject.transaction import Transaction


# tests if User inserts approved bank card by three banks allowed by the bank
def test_bank_card_verifies_if_approved_by_bank():
    valid_names = [
        "RBC",
        "ScotiaBank",
        "BMO",
    ]

    bankcard = BankCard()
    for bank_name in valid_names:
        assert bankcard.verify_approval(bank_name) == True, "date should be verified as valid"


# tests for invalid bank card
def test_credit_card_fails_invalid_names():
    invalid_names = [
        "CIBC",
        "aaaaa",
        None
    ]

    bankcard = BankCard()
    for bank_name in invalid_names:
        assert bankcard.verify_approval(bank_name) == False, "date should not be verified, it is false"


# tests for valid bank accounts checking and savings
def test_bank_account():
    valid_accounts = [
        "Checking"
        "Savings"
    ]

    bankcard = BankCard()

    for account in valid_accounts:
        assert bankcard.check_account(account) == True, "Bank Account must be checking or savings"


# tests for no bank accounts valid with the account
def test_bank_invalid_account():
    invalid_account = [
        "aaaa",
        None
    ]
    bankcard = BankCard()

    for account in invalid_account:
        assert bankcard.check_account(
            account) == False, "No account found"  # "If bank account does not have checking or savings, it will fail (i.e no account)"


# tests withdrawal in appropriate denominations
def test_withdraw_money():
    valid_denominations = [
        "5",
        "10",
        "20"
        "50"
        "100"
    ]
    transaction = Transaction()

    for amount in valid_denominations:
        assert transaction.withdraw_money(amount) == True, "Amount Accepted"


# tests for invalid amount if user does not select appropriate denomination
def test_withdraw_money_invalid_amount():
    invalid_denominations = [
        "1",
        "2",
        "3",
        "4",
        "94",
        "86",
    ]
    transaction = Transaction()

    for amount in invalid_denominations:
        assert transaction.withdraw_money(amount) == False, "Invalid Number"


# tests for two different transactions
def test_transaction_choice():
    valid_transaction_types = [
        "Withdrawal",
        "Deposit Cheque"
    ]
    transaction = Transaction()

    for choice in valid_transaction_types:
        assert transaction.transaction_type(choice) == True, "Please choose from the following two Transactions"


# tests for if user does not select a choice for transaction
def test_transaction_incorrect_choice():
    invalid_choice = [
        "aa",
        None
    ]

    transaction = Transaction()

    for choice in invalid_choice:
        assert transaction.transaction_type(choice) == False, "Incorrect Choice"


# tests for account balance
def test_account_balance():
    balance_current = [
        "100",
        "20000",
        "95000",
        "1"
    ]

    transaction = Transaction()

    for balance in balance_current:
        assert transaction.account_balance(balance) == True, "User has money in account"


# tests for an empty account balance
def test_account_balance_null():
    bank_account_is_empty = [
        "0",
        "-100",
        None,
    ]

    transaction = Transaction()

    for balance in bank_account_is_empty:
        assert transaction.account_balance(balance) == False, "User has no money in account"


# tests for money being deposited into an account via cheque
def test_add_money_to_account():
    cheque_verified_amount = [
        "100",
        "1000",
        "1123"
    ]

    transaction = Transaction()

    for deposit_amount in cheque_verified_amount:
        assert transaction.cheque_deposit_account_update(
            deposit_amount) == True, "Cheque has been verified and amount is added"


# tests for verfication on cheque
def test_cheque_verfication():
    cheque_verfication = [
        "bank approved",
        "RBC",
        "CIBC",
    ]

    transaction = Transaction()

    for approval in cheque_verfication:
        assert transaction.cheque_verfication(approval) == True, "Cheque is approved"


# tests for invalid cheque(verification failed)
def test_cheque_verification_failed():
    cheque_verification_failed = [
        "China",
        "Michael Jackson",
        "Vince Mcmahon",
    ]

    transaction = Transaction()

    for approval in cheque_verification_failed:
        assert transaction.cheque_verfication(approval) == False, "Cheque has not been recognizes by the system"


# tests for balance after transaction is completed
def test_account_balance_after_transaction():
    balance_after_transaction = [
        "1",
        "10000",
        "25000",
        "45982",
        "4",
    ]

    transaction = Transaction()

    for balance in balance_after_transaction:
        assert transaction.account_balance_post_transaction(balance) == True, "Account Balance is displayed"


# tests for if user empties bank account after transaction is completed
def test_account_balance_after_transaction_is_empty():
    balance_after_transaction_empty = [
        "0",
        None
    ]

    transaction = Transaction()

    for balance in balance_after_transaction_empty:
        assert transaction.account_balance_post_transaction(balance) == False, "Account balance is now empty"


# tests for if user does no make a selection for money customization
def test_default_selection():
    default_selection = [
        "20"
    ]

    transaction = Transaction()

    for amount in default_selection:
        assert transaction.default_selection_withdraw(amount) == True, "User has made no selection, default is $20"


# tests for always rounding down if user does not select the right denomination
def test_withdraw_round_down():
    withdrawal_amount = [
        "48"
        "21"
        "53"
    ]

    transaction = Transaction()

    for amount in withdrawal_amount:
        assert transaction.withdraw_round(amount) == True, "The system will round down to the nearest $5"


# tests for transaction number under 3
def test_transaction_limit():
    transaction_number = [
        "1"
        "2"
        "3"
    ]

    transaction = Transaction()

    for number in transaction_number:
        assert transaction.transaction_limit_for_day(number) == True, "The limit of transactions has not been reached"


# tests for transaction number over 3
def test_transaction_limit_exceeded():
    transaction_number_exceeded = [
        "4"
        "5"
        "6"
        "7"
        "10"
        "12"
    ]

    transaction = Transaction()

    for number in transaction_number_exceeded:
        assert transaction.transaction_limit_for_day(number) == False, "The limit of transactions has been reached"


# test for transaction being completed by a transaction number being issued by the system
def test_transaction_is_complete():
    transaction_complete_confirm = [
        "1231231"
        "123134545"
        "123124423"
        "456456"

    ]

    transaction = Transaction()

    for transaction_number in transaction_complete_confirm:
        assert transaction.transaction_completed(transaction_number) == True, "Transaction is complete"


# test for removal of bills
def test_removing_bills():
    bill_to_remove = [
        "5"
        "10"
        "20"
    ]

    transaction = Transaction()

    for value in bill_to_remove:
        assert transaction.note_removal(value) == True, "The bank note has successfully been removed"


