import pytest
from employee import Employee


@pytest.fixture
def employee_ins():
    """Return employee instance"""
    employee_ins = Employee("Rupashri", "Mohan", "150000")
    return employee_ins


def test_give_default_raise(employee_ins):
    "Testing the raise amount with default raise"
    employee_ins.give_raise()
    assert employee_ins.updated_salary == 155000


def test_give_custom_raise(employee_ins):
    "Testing the raise amount with default raise"
    employee_ins.give_raise(7000)
    assert employee_ins.updated_salary == 157000
