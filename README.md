# Personal Finance Manager - Design Patterns Project

This project is a hands-on exercise in applying Object-Oriented Design Patterns to build a simplified personal finance manager.
You will implement and extend starter code to add functionality such as tracking transactions, adapting external data, observing balance changes, and ensuring proper architectural patterns.

## Getting Started

### Dependencies

Make sure you have python version >= 3.10.x installed on your computer.

### Installation

1. Clone the repo:

    ```bash
    git clone https://github.com/udacity/cd14600-project-starter.git
    cd cd14600-project-starter/starter
    ```

2. Run the Program:

    ```bash
    python main.py
    ```

## Project Structure

```txt
starter/
├── main.py                          # Entry point and composition root
├── balance/
│   ├── balance.py                   # Singleton Balance class
│   ├── balance_observer.py          # Observer interface + PrintObserver, LowBalanceAlertObserver
│   ├── test_balance.py              # Tests for Balance
│   └── test_balance_observer.py     # Tests for observers
├── transaction/
│   ├── transaction.py               # Transaction domain model
│   ├── transaction_category.py      # TransactionCategory enum (INCOME, EXPENSE)
│   ├── transaction_adapter.py       # Adapter for external transactions
│   ├── external_income_transaction.py  # External data source
│   ├── test_transaction.py          # Tests for Transaction
│   └── test_transaction_adapter.py  # Tests for Adapter
└── strategy/
    ├── budget_strategy.py           # Strategy pattern (IBudgetStrategy + implementations)
    └── test_budget_strategy.py      # Tests for strategies
```

## Testing

This project uses Python's built-in unittest framework. All tests run from the `starter/` directory.

To run all tests (17 tests):

```bash
python -m unittest discover
```

To run a single test file:

```bash
python -m unittest balance.test_balance_observer
```

### Break Down Tests

- test_balance.py → Verifies correct implementation of the Singleton Balance class.
- test_transaction.py → Confirms Transaction construction, string representation, equality, and hashability.
- test_transaction_adapter.py → Ensures external income data is correctly adapted into Transaction objects.
- test_balance_observer.py → Validates that low-balance alerts trigger at the correct threshold and that PrintObserver outputs the expected message.
- test_budget_strategy.py → Validates budget allocation math and strategy interchangeability.

## Project Instructions

1. Implement Singleton Balance Class – Ensure only one balance object exists throughout the app.
2. Complete Transaction Class – Handle income and expense transactions.
3. Implement Adapter Pattern – Adapt external freelance income data into internal Transaction objects.
4. Implement Observer Pattern – Create a low balance observer that triggers an alert when funds drop too low.
5. Add Unit Tests – Write tests for all implemented functionality.
6. Choose and Implement a Fourth Pattern – Pick one additional design pattern (e.g., Strategy, Command, Decorator, etc.) and integrate it into your project.
7. Provide a Reflection – Add a short write-up in your repo (README or separate file) explaining your design choices.

## Built With

- [Python](https://www.python.org/) – Main programming language
- [unittest](https://docs.python.org/3/library/unittest.html) – Testing framework
- [PEP8](https://peps.python.org/pep-0008/) – Style guide for Python code

## License

[License](LICENSE.md)
