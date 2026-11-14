"""Validated ATM withdrawal helpers for Lab 7 fuzz testing."""

DAILY_LIMIT = {"savings": 25_000, "current": 50_000}


def _require_integer(value, field_name):
    """Raise ValueError unless value is an integer but not a boolean."""
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{field_name} must be an integer")


def withdraw(balance, amount, account_type, own_bank):
    """Return the post-withdrawal balance or a status message."""
    _require_integer(balance, "balance")
    _require_integer(amount, "amount")

    if balance < 0:
        raise ValueError("balance cannot be negative")
    if amount <= 0 or amount % 100 != 0:
        raise ValueError("amount must be a positive multiple of 100")
    if not isinstance(account_type, str) or account_type not in DAILY_LIMIT:
        raise ValueError("unknown account")
    if not isinstance(own_bank, bool):
        raise ValueError("own_bank must be a boolean")

    if amount > DAILY_LIMIT[account_type]:
        return "limit exceeded"

    fee = 0
    if not own_bank:
        fee = 20
        if amount > 10_000:
            fee += 10

    total_debit = amount + fee
    if total_debit > balance:
        return "insufficient funds"
    return balance - total_debit


def pin_check(entered, actual, attempts):
    """Check a PIN and return ok, retry, or card blocked."""
    _require_integer(entered, "entered PIN")
    _require_integer(actual, "actual PIN")
    _require_integer(attempts, "attempts")

    if entered < 0 or actual < 0:
        raise ValueError("PIN values cannot be negative")
    if attempts < 0:
        raise ValueError("attempts cannot be negative")

    if attempts >= 3:
        return "card blocked"
    if entered == actual:
        return "ok"
    if attempts == 2:
        return "card blocked"
    return "retry"


def note_breakup(amount):
    """Return the number of 500, 200, and 100 currency notes required."""
    _require_integer(amount, "amount")
    if amount < 0 or amount % 100 != 0:
        raise ValueError("amount must be a non-negative multiple of 100")

    notes_500, remaining = divmod(amount, 500)
    notes_200, remaining = divmod(remaining, 200)
    notes_100 = remaining // 100
    return notes_500, notes_200, notes_100


def main():
    """Run a short demonstration of the ATM operations."""
    print("ATM Withdrawal Processor")
    print("Withdrawal:", withdraw(20_000, 5_000, "savings", True))
    print("PIN check:", pin_check(1234, 1234, 0))
    print("Note breakup (1,200):", note_breakup(1_200))


if __name__ == "__main__":
    main()
