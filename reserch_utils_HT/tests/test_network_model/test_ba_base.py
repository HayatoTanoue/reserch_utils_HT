import pytest
from reserch_utils_HT.src.network_model.ba_base import sample_model


def test_sample_model():
    assert sample_model() == 2
