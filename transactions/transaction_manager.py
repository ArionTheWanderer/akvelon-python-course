import os.path
import pickle
from .invalid_transaction_input_exception import *
from functools import reduce


class TransactionManager:

    # Вынес вывод результата в отдельный метод. Нижнее подчеркивание показывает, что снаружи метод лучше не трогать
    # т.к. "результат не предсказуем"
    @staticmethod
    def _print_result(transactions):
        print("Transaction types: ")
        total = 0
        for t in transactions:
            if len(transactions[t]) != 0:
                transaction_summary = reduce(lambda x, y: x + y, transactions[t])
            else:
                transaction_summary = 0
            total += transaction_summary
            print(f"{t}: {transaction_summary}")
        print(f"Total is {total}")

    # Можно передать свое названия файла для сохранения транзаций, но также задано значение по умолчанию
    @staticmethod
    def make_transaction(file_to_save="transactions_saved.pkl"):
        if os.path.exists(file_to_save):
            with open(file_to_save, "rb") as f:
                transactions = pickle.load(f)
        else:
            transactions = {
                "Restaurants": [],
                "Hotels": [],
                "Cafes": []
            }
        print("Transactions list and the amount money spent:")
        for t in transactions:
            print(f"{t}: {transactions[t]}")

        run = True
        inp_raw = input("Please, input the type of transaction and the amount of money spent. Wanna quit? Input "
                        "'quit'\n")
        while run:
            split_input = str.split(inp_raw, " ")
            try:
                money_spent = int(split_input.pop())
            except ValueError as e:
                print(f"Invalid integer value. Error: {e}")
                raise InvalidTransactionException("Can't parse the amount of money. Wrong format.")
            transaction_name = split_input.pop()
            for part in split_input:
                transaction_name = part + " " + transaction_name
            if transaction_name not in transactions:
                raise InvalidTransactionException("Can’t parse the transaction name properly.")
            transactions[transaction_name].append(money_spent)
            inp_raw = input("Please, input the type of transaction and the amount of money spent. Wanna quit? Input "
                            "'quit'\n")
            if inp_raw == "quit":
                run = False

        with open(file_to_save, "wb") as f:
            pickle.dump(transactions, f)
        TransactionManager._print_result(transactions)
