"""Hypothesis fuzz tests for the ATM withdrawal module (Lab 7)."""

import pytest
from hypothesis import HealthCheck, assume, given, settings, strategies as st

from atm_withdrawal import DAILY_LIMIT, note_breakup, pin_check, withdraw


FUZZ_SETTINGS = settings(
    max_examples=150,
    deadline=None,
    suppress_health_check=[HealthCheck.too_slow],
)

INTEGER_BUT_NOT_BOOL = st.integers()
INVALID_SCALAR = st.one_of(
    st.none(),
    st.booleans(),
    st.text(max_size=12),
    st.floats(allow_nan=False, allow_infinity=False),
    st.lists(st.integers(), max_size=3),
    st.dictionaries(st.text(max_size=3), st.integers(), max_size=2),
)


@FUZZ_SETTINGS
@given(
    balance=st.integers(min_value=0, max_value=1_000_000),
    amount=st.integers(min_value=1, max_value=600).map(lambda value: value * 100),
    account_type=st.sampled_from(tuple(DAILY_LIMIT)),
    own_bank=st.booleans(),
)
def test_withdraw_matches_expected_rules(balance, amount, account_type, own_bank):
    fee = 0 if own_bank else 20 + (10 if amount > 10_000 else 0)
    if amount > DAILY_LIMIT[account_type]:
        expected = "limit exceeded"
    elif amount + fee > balance:
        expected = "insufficient funds"
    else:
        expected = balance - amount - fee
    assert withdraw(balance, amount, account_type, own_bank) == expected


@FUZZ_SETTINGS
@given(balance=st.integers(max_value=-1))
def test_withdraw_rejects_negative_balance(balance):
    with pytest.raises(ValueError):
        withdraw(balance, 100, "savings", True)


@FUZZ_SETTINGS
@given(value=INVALID_SCALAR)
def test_withdraw_rejects_invalid_balance_types(value):
    assume(not isinstance(value, int) or isinstance(value, bool))
    with pytest.raises(ValueError):
        withdraw(value, 100, "savings", True)


@FUZZ_SETTINGS
@given(value=INVALID_SCALAR)
def test_withdraw_rejects_invalid_amount_types(value):
    assume(not isinstance(value, int) or isinstance(value, bool))
    with pytest.raises(ValueError):
        withdraw(10_000, value, "savings", True)


@FUZZ_SETTINGS
@given(amount=st.integers().filter(lambda value: value <= 0 or value % 100 != 0))
def test_withdraw_rejects_nonpositive_or_non_hundred_amounts(amount):
    with pytest.raises(ValueError):
        withdraw(100_000, amount, "savings", True)


@FUZZ_SETTINGS
@given(account_type=st.one_of(st.none(), st.lists(st.text()), st.text().filter(lambda value: value not in DAILY_LIMIT)))
def test_withdraw_rejects_unknown_account_types(account_type):
    with pytest.raises(ValueError):
        withdraw(100_000, 100, account_type, True)


@FUZZ_SETTINGS
@given(own_bank=INVALID_SCALAR)
def test_withdraw_rejects_non_boolean_bank_flag(own_bank):
    assume(not isinstance(own_bank, bool))
    with pytest.raises(ValueError):
        withdraw(100_000, 100, "savings", own_bank)


@FUZZ_SETTINGS
@given(
    entered=st.integers(min_value=0, max_value=99_999),
    actual=st.integers(min_value=0, max_value=99_999),
    attempts=st.integers(min_value=0, max_value=10),
)
def test_pin_check_returns_only_valid_status(entered, actual, attempts):
    result = pin_check(entered, actual, attempts)
    if attempts >= 3 or (attempts == 2 and entered != actual):
        assert result == "card blocked"
    elif entered == actual:
        assert result == "ok"
    else:
        assert result == "retry"


@FUZZ_SETTINGS
@given(value=INVALID_SCALAR)
def test_pin_check_rejects_invalid_entered_pin_types(value):
    assume(not isinstance(value, int) or isinstance(value, bool))
    with pytest.raises(ValueError):
        pin_check(value, 1234, 0)


@FUZZ_SETTINGS
@given(value=INVALID_SCALAR)
def test_pin_check_rejects_invalid_actual_pin_types(value):
    assume(not isinstance(value, int) or isinstance(value, bool))
    with pytest.raises(ValueError):
        pin_check(1234, value, 0)


@FUZZ_SETTINGS
@given(value=st.integers(max_value=-1))
def test_pin_check_rejects_negative_pin_values(value):
    with pytest.raises(ValueError):
        pin_check(value, 1234, 0)


@FUZZ_SETTINGS
@given(attempts=st.integers(max_value=-1))
def test_pin_check_rejects_negative_attempt_counts(attempts):
    with pytest.raises(ValueError):
        pin_check(1234, 1234, attempts)


@FUZZ_SETTINGS
@given(value=INVALID_SCALAR)
def test_pin_check_rejects_invalid_attempt_types(value):
    assume(not isinstance(value, int) or isinstance(value, bool))
    with pytest.raises(ValueError):
        pin_check(1234, 1234, value)


@FUZZ_SETTINGS
@given(amount=st.integers(min_value=0, max_value=10_000_000).map(lambda value: value * 100))
def test_note_breakup_conserves_amount(amount):
    notes_500, notes_200, notes_100 = note_breakup(amount)
    assert min(notes_500, notes_200, notes_100) >= 0
    assert notes_500 * 500 + notes_200 * 200 + notes_100 * 100 == amount


@FUZZ_SETTINGS
@given(amount=st.integers().filter(lambda value: value < 0 or value % 100 != 0))
def test_note_breakup_rejects_negative_or_non_hundred_amounts(amount):
    with pytest.raises(ValueError):
        note_breakup(amount)


@FUZZ_SETTINGS
@given(value=INVALID_SCALAR)
def test_note_breakup_rejects_invalid_input_types(value):
    assume(not isinstance(value, int) or isinstance(value, bool))
    with pytest.raises(ValueError):
        note_breakup(value)
