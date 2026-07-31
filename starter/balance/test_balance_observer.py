import unittest
from unittest.mock import patch

from balance.balance import Balance
from balance.balance_observer import LowBalanceAlertObserver, PrintObserver
from transaction.transaction import Transaction
from transaction.transaction_category import TransactionCategory


class TestLowBalanceAlertObserver(unittest.TestCase):

    def setUp(self):
        self.balance = Balance.get_instance()
        self.balance.reset()

    def test_alert_triggers_on_low_balance(self):
        observer = LowBalanceAlertObserver(threshold=50)
        self.balance.register_observer(observer)

        self.balance.apply_transaction(
            Transaction(100, TransactionCategory.INCOME)
        )
        self.assertFalse(observer.alert_triggered)

        self.balance.apply_transaction(
            Transaction(60, TransactionCategory.EXPENSE)
        )
        self.assertTrue(observer.alert_triggered)

        self.balance.apply_transaction(
            Transaction(100, TransactionCategory.INCOME)
        )
        self.assertFalse(observer.alert_triggered)

        self.balance.apply_transaction(
            Transaction(60, TransactionCategory.EXPENSE)
        )
        self.assertFalse(observer.alert_triggered)

        self.balance.apply_transaction(
            Transaction(60, TransactionCategory.EXPENSE)
        )
        self.assertTrue(observer.alert_triggered)


class TestPrintObserver(unittest.TestCase):

    def setUp(self):
        self.balance = Balance.get_instance()
        self.balance.reset()

    @patch('builtins.print')
    def test_print_observer_output(self, mock_print):
        observer = PrintObserver()
        self.balance.register_observer(observer)

        self.balance.apply_transaction(
            Transaction(100, TransactionCategory.INCOME)
        )

        mock_print.assert_called_once_with(
            "[Income] 100 -> Balance: $100.0"
        )


if __name__ == "__main__":
    unittest.main()
