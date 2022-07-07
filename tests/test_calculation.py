import pytest

# pylint: disable=redefined-outer-name
from example.calculation import Calculcation


@pytest.fixture
def calculation_simple():
    return Calculcation(10, 2)


def test_add(calculation_simple):
    assert calculation_simple.add() == 12
