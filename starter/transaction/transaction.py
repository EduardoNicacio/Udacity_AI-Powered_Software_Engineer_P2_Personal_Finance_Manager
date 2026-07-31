# transaction.py

from transaction.transaction_category import TransactionCategory


class Transaction:
    """Represents a financial transaction with an amount and category."""

    def __init__(self, amount, category, invoice_id=None, description=None):
        self.amount = amount
        self.category = category
        self.invoice_id = invoice_id
        self.description = description

    def __str__(self):
        base = f"Transaction(${self.amount}, category='{self.category}')"
        if self.invoice_id is not None:
            base += f", invoice_id='{self.invoice_id}'"
        if self.description is not None:
            base += f", description='{self.description}'"
        return base

    def __eq__(self, other):
        if not isinstance(other, Transaction):
            return False
        return (
            self.amount == other.amount
            and self.category == other.category
            and self.invoice_id == other.invoice_id
            and self.description == other.description
        )

    def __hash__(self):
        return hash(
            (
                self.amount,
                self.category,
                self.invoice_id,
                self.description,
            )
        )
