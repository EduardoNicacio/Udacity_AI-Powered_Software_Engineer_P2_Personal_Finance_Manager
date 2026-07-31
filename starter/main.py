"""This module serves as the entry point for the program."""
from balance.balance import Balance
from balance.balance_observer import LowBalanceAlertObserver
from balance.balance_observer import PrintObserver
from strategy.budget_strategy import FiftyThirtyTwentyStrategy
from transaction.transaction import Transaction
from transaction.transaction_category import TransactionCategory
from transaction.transaction_adapter import TransactionAdapter
from transaction.external_income_transaction import ExternalFreelanceIncome


def main():
    print("Adding transactions...")

    # Create the singleton Balance instance.
    balance = Balance.get_instance()

    # Dependency injection: observers are constructed outside and
    # registered on the Balance, keeping it decoupled from alerting logic.
    low_balance_observer = LowBalanceAlertObserver(threshold=200)
    print_observer = PrintObserver()
    balance.register_observer(low_balance_observer)
    balance.register_observer(print_observer)

    # Create standard transactions
    transactions = [
        Transaction(100, TransactionCategory.INCOME),
        Transaction(50, TransactionCategory.EXPENSE),
        Transaction(200, TransactionCategory.INCOME),
        Transaction(75, TransactionCategory.EXPENSE),
    ]

    # Create an external income transaction (via Adapter pattern)
    freelance_income = ExternalFreelanceIncome(1200, "INV-98765", "Mobile App Project")
    adapter = TransactionAdapter(freelance_income)
    adapted_transaction = adapter.to_transaction()

    all_transactions = transactions + [adapted_transaction]

    # Apply all transactions to balance
    for txn in all_transactions:
        balance.apply_transaction(txn)

    print()
    print(balance.summary())
    print(
        "Low balance alert triggered: "
        f"{low_balance_observer.alert_triggered}"
    )

    # Demonstrate the Strategy pattern for budget planning.
    print()
    print("Budget allocation (50/30/20 rule):")
    strategy = FiftyThirtyTwentyStrategy()
    allocation = strategy.execute(balance.get_balance())
    for category, amount in allocation.items():
        print(f"  {category}: ${amount:.2f}")


if __name__ == "__main__":
    main()
