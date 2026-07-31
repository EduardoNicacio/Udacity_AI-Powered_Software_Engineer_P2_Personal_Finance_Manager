# budget_strategy.py


class IBudgetStrategy:
    def execute(self, balance):
        """Compute a budget allocation for the given balance.

        Args:
            balance (float): The total amount to allocate.

        Returns:
            dict: A mapping of category names to allocated amounts.
        """
        raise NotImplementedError("Subclasses must implement execute method.")


class FiftyThirtyTwentyStrategy(IBudgetStrategy):
    """Allocate balance using the 50/30/20 rule: 50% needs, 30% wants, 20% savings."""

    def execute(self, balance):
        return {
            "needs": balance * 0.50,
            "wants": balance * 0.30,
            "savings": balance * 0.20,
        }


class ZeroBasedBudgetStrategy(IBudgetStrategy):
    """Allocate every dollar of the balance to specific categories (sum == balance)."""

    def execute(self, balance):
        return {
            "housing": balance * 0.35,
            "food": balance * 0.25,
            "transport": balance * 0.15,
            "savings": balance * 0.25,
        }
