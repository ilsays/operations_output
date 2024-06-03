from utils.functions import mask_card_number
import pytest


def test_mask_card_number():
    assert mask_card_number('6831982476737658') == '6831 98** **** 7658'
    assert mask_card_number('5999414228426353') == '5999 41** **** 6353'
