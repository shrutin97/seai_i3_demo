import pytest
from calculations import *
import numpy as np


def test_greeting():
    assert 'Have a nice day Mukunda!' == greeting('mukunda')


def test_product():
    assert 40 == product(5, 8)


def test_sum():
    assert 123 == adder(10, 2)


def test_matrix_multiply_res():
    a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    b = np.array([[10, 20, 30], [40, 50, 60], [1, 2, 3]])
    res = np.array([[93, 126, 159],
                    [246, 342, 438],
                    [399, 558, 717]])
    assert (res == matrix_multiply(a, b)).all()


def test_matrix_multiply_res():
    a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    b = np.array([[10, 20, 30], [40, 50, 60], [1, 2, 3]])
    assert a.shape[1] == b.shape[0]
