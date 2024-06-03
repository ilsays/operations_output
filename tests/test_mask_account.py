from utils.functions import mask_account
import pytest


def test_mask_account():
    assert mask_account('Счет 72082042523231456215') == '**6215'
    assert mask_account('Счет 72731966109147704472') == '**4472'
