import unittest

from strategy.budget_strategy import (
    FiftyThirtyTwentyStrategy,
    IBudgetStrategy,
    ZeroBasedBudgetStrategy,
)


class TestBudgetStrategy(unittest.TestCase):

    def test_fifty_thirty_twenty_allocation(self):
        strategy = FiftyThirtyTwentyStrategy()
        result = strategy.execute(1000)
        self.assertEqual(result["needs"], 500)
        self.assertEqual(result["wants"], 300)
        self.assertEqual(result["savings"], 200)
        self.assertEqual(sum(result.values()), 1000)

    def test_zero_based_budget_allocation(self):
        strategy = ZeroBasedBudgetStrategy()
        result = strategy.execute(1000)
        self.assertEqual(result["housing"], 350)
        self.assertEqual(result["food"], 250)
        self.assertEqual(result["transport"], 150)
        self.assertEqual(result["savings"], 250)
        self.assertEqual(sum(result.values()), 1000)

    def test_strategy_interchangeability(self):
        """Both strategies can be used through the common interface."""
        balance = 1000
        for strategy in (FiftyThirtyTwentyStrategy(), ZeroBasedBudgetStrategy()):
            self.assertIsInstance(strategy, IBudgetStrategy)
            result = strategy.execute(balance)
            self.assertAlmostEqual(sum(result.values()), balance)


if __name__ == "__main__":
    unittest.main()
