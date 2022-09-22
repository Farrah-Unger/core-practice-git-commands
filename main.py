import pytest


def always_returns_true():
    return True


def test_always_returns_true():
    #act 
    always_returns_true()
    #assert
    assert always_returns_true() == True
