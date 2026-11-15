"""Tests intended to achieve high statement (code) coverage."""

import pytest

from atm_withdrawal import note_breakup, pin_check, withdraw


def test_withdraw_rejects_unknown_account():
    with pytest.raises(ValueError, match="unknown account"):
        withdraw(5000, 1000, "business", True)


def test_withdraw_rejects_invalid_amounts():
    with pytest.raises(ValueError, match="invalid amount"):
        withdraw(5000, 0, "savings", True)
    with pytest.raises(ValueError, match="invalid amount"):
        withdraw(5000, 150, "savings", True)


def test_withdraw_daily_limit_exceeded():
    assert withdraw(60000, 25100, "savings", True) == "limit exceeded"


def test_withdraw_own_bank_success():
    assert withdraw(5000, 1000, "savings", True) == 4000


def test_withdraw_other_bank_success_and_fees():
    assert withdraw(5000, 1000, "savings", False) == 3980
    assert withdraw(20000, 11000, "current", False) == 8970


def test_withdraw_insufficient_funds():
    assert withdraw(1000, 1000, "savings", False) == "insufficient funds"


def test_pin_check_paths():
    assert pin_check(1234, 1234, 0) == "ok"
    assert pin_check(1111, 1234, 0) == "retry"
    assert pin_check(1111, 1234, 2) == "card blocked"
    assert pin_check(1234, 1234, 3) == "card blocked"


def test_note_breakup_paths():
    assert note_breakup(700) == (1, 1, 0)
    assert note_breakup(0) == (0, 0, 0)
    assert note_breakup(600) == (1, 0, 1)
    with pytest.raises(ValueError, match="invalid amount"):
        note_breakup(650)
