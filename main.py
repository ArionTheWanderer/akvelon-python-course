import transactions


if __name__ == '__main__':
    try:
        transactions.TransactionManager.make_transaction()
    except transactions.InvalidTransactionException as e:
        print(f"Transaction parse error. Error: {e}")
