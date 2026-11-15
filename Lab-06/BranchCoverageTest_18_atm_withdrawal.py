"""Tests designed to exercise both outcomes of each decision branch."""

import pytest

from atm_withdrawal import note_breakup, pin_check, withdraw


def test_account_type_branches():
    with pytest.raises(ValueError, match="unknown account"):
        withdraw(10000, 1000, "business", True)
    assert withdraw(5000, 1000, "savings", True) == 4000


def test_amount_validation_branches():
    with pytest.raises(ValueError, match="invalid amount"):
        withdraw(5000, 0, "savings", True)
    with pytest.raises(ValueError, match="invalid amount"):
        withdraw(5000, 150, "savings", True)
    assert withdraw(5000, 1000, "savings", True) == 4000


def test_daily_limit_true_and_false():
    assert withdraw(60000, 25100, "savings", True) == "limit exceeded"
    assert withdraw(5000, 1000, "savings", True) == 4000


def test_own_bank_and_other_bank_fee_branches():
    assert withdraw(5000, 1000, "savings", True) == 4000
    assert withdraw(5000, 1000, "savings", False) == 3980
    assert withdraw(20000, 10000, "current", False) == 9980
    assert withdraw(20000, 10100, "current", False) == 9870


def test_sufficient_and_insufficient_balance_branches():
    assert withdraw(5000, 1000, "savings", True) == 4000
    assert withdraw(1000, 1000, "savings", False) == "insufficient funds"


def test_pin_check_branches():
    assert pin_check(1234, 1234, 3) == "card blocked"
    assert pin_check(1234, 1234, 0) == "ok"
    assert pin_check(9999, 1234, 0) == "retry"
    assert pin_check(9999, 1234, 2) == "card blocked"


def test_note_breakup_branches():
    with pytest.raises(ValueError, match="invalid amount"):
        note_breakup(650)
    assert note_breakup(700) == (1, 1, 0)
    assert note_breakup(0) == (0, 0, 0)
    assert note_breakup(600) == (1, 0, 1)
