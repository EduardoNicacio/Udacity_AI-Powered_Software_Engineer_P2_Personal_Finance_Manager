import unittest

from transaction.transaction import Transaction
from transaction.transaction_category import TransactionCategory


class TestTransaction(unittest.TestCase):

    def test_transaction_creation(self):
        t = Transaction(100, TransactionCategory.EXPENSE)
        self.assertEqual(t.amount, 100)
        self.assertEqual(t.category, TransactionCategory.EXPENSE)

    def test_transaction_str(self):
        t = Transaction(50, TransactionCategory.INCOME)
        expected = "Transaction($50, category='TransactionCategory.INCOME')"
        self.assertEqual(str(t), expected)

    def test_transaction_equality(self):
        t1 = Transaction(20, TransactionCategory.EXPENSE)
        t2 = Transaction(20, TransactionCategory.EXPENSE)
        t3 = Transaction(30, TransactionCategory.EXPENSE)
        self.assertEqual(t1, t2)
        self.assertNotEqual(t1, t3)

    def test_transaction_metadata(self):
        t = Transaction(
            100,
            TransactionCategory.INCOME,
            invoice_id="INV-001",
            description="Consulting",
        )
        self.assertEqual(t.invoice_id, "INV-001")
        self.assertEqual(t.description, "Consulting")

    def test_transaction_metadata_none_by_default(self):
        t = Transaction(50, TransactionCategory.EXPENSE)
        self.assertIsNone(t.invoice_id)
        self.assertIsNone(t.description)

    def test_transaction_metadata_equality(self):
        t1 = Transaction(
            100,
            TransactionCategory.INCOME,
            invoice_id="INV-001",
            description="A",
        )
        t2 = Transaction(
            100,
            TransactionCategory.INCOME,
            invoice_id="INV-002",
            description="A",
        )
        self.assertNotEqual(t1, t2)


if __name__ == "__main__":
    unittest.main()
