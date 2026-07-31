# transaction_adapter.py

from transaction.transaction import Transaction
from transaction.transaction_category import TransactionCategory

class TransactionAdapter:
    def __init__(self, external_transaction):
        self.external_transaction = external_transaction

    def to_transaction(self):
        """Convert an external transaction to a standard Transaction."""
        if self.external_transaction.typ == "income":
            category = TransactionCategory.INCOME
        elif self.external_transaction.typ == "expense":
            category = TransactionCategory.EXPENSE
        else:
            raise ValueError(
                f"Invalid transaction type: {self.external_transaction.typ}"
            )
        return Transaction(
            amount=self.external_transaction.amount,
            category=category,
        )
