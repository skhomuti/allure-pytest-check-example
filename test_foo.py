import pytest_check as check


def test_check():
    check.equal(1, 2)


def test_simple():
    assert 1 == 2
