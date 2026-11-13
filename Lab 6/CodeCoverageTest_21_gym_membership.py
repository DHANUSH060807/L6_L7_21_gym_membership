import pytest
from gym_membership import membership_cost, can_enter, bmi_category


# Membership cost tests
def test_regular_monthly_plan():
    assert membership_cost("monthly", 30, False, False) == 1500


def test_senior_discount():
    assert membership_cost("quarterly", 65, False, False) == 3000


def test_student_discount():
    assert membership_cost("monthly", 20, True, False) == 1350


def test_yearly_trainer_discount():
    assert membership_cost("yearly", 30, False, True) == 13500


def test_invalid_plan():
    with pytest.raises(ValueError, match="unknown plan"):
        membership_cost("weekly", 30, False, False)


def test_too_young():
    with pytest.raises(ValueError, match="too young"):
        membership_cost("monthly", 12, False, False)


# Gym entry tests
def test_inactive_plan():
    assert can_enter(10, False, False, "M") is False


def test_invalid_hours():
    assert can_enter(3, True, False, "M") is False


def test_women_only_slot():
    assert can_enter(10, True, True, "F") is True


def test_women_only_slot_male():
    assert can_enter(10, True, True, "M") is False


def test_normal_entry():
    assert can_enter(10, True, False, "M") is True


# BMI category tests
def test_invalid_height():
    with pytest.raises(ValueError, match="invalid height"):
        bmi_category(70, 0)


def test_underweight():
    assert bmi_category(50, 1.8) == "underweight"


def test_normal_bmi():
    assert bmi_category(70, 1.75) == "normal"


def test_overweight():
    assert bmi_category(80, 1.7) == "overweight"


def test_obese():
    assert bmi_category(100, 1.7) == "obese"