import pytest
from put_stress_rus.put_stress import put_stress


def test_put_stress():
    assert "селё'дка" == put_stress("селёдка") 