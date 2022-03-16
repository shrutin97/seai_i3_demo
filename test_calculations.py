import pytest
from calculations import *


def test_greeting():
    assert 'Have a nice day mukunda!' == greeting('mukunda')
