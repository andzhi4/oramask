from oramask import ora_to_sft, sft_to_ora
import pytest 


@pytest.mark.parametrize(('input', 'result'),
    (
        ('HH24:MI:SS', '%H:%M:%S'),
        ('HH12:MI:SS', '%I:%M:%S'),
        ('DD-MON-YYYY HH24:MI:SS', '%d-%b-%Y %H:%M:%S'),
        ('YYYY/MM/DD', '%Y/%m/%d'),
        ('', ''),
    )
)
def test_ora_to_sft(input, result):
    assert ora_to_sft(input) == result


@pytest.mark.parametrize(('input', 'result'),
                         (
    ('%H:%M:%S', 'HH:MI:SS'),
)
)
def test_sft_to_ora(input, result):
    assert sft_to_ora(input) == result
