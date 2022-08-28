from put_stress_rus.put_stress import put_stress


def test_put_stress():
    output = "Input word includes invalid character, remove it and try again"
    assert "селё'дка" == put_stress("селёдка")
    assert output == put_stress("не ставь проблел")
