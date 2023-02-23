from oramask import ora_to_sft, sft_to_ora
import pytest 


@pytest.mark.parametrize(('input', 'result'),
    (
        ('', ''),
        ('HH24:MI:SS', '%H:%M:%S'),
        ('HH12:MI:SS', '%I:%M:%S'),
        ('DD-MON-YYYY HH24:MI:SS', '%d-%b-%Y %H:%M:%S'),
        ('YYYY/MM/DD', '%Y/%m/%d'),
        ('YYYY-MM-DD HH12:MI:SSSS TZ', '%Y-%m-%d %I:%M:%f %Z'),
        ('YYYYMMDD', '%Y%m%d'),
        ('HH24MISS', '%H%M%S'),
        ('YYYYMMDDHH24MISS', '%Y%m%d%H%M%S'),
        ('hh12:mi:ss', '%I:%M:%S'),

    )
)
def test_ora_to_sft(input, result):
    assert ora_to_sft(input) == result


@pytest.mark.parametrize(('input', 'result'),
                         (
    ('', ''),
    ('%H:%M:%S', 'HH24:MI:SS'),
    ('%H%M%S', 'HH24MISS'),
    ('%Y%m%d', 'YYYYMMDD'),
    ('%Y%m%d%H%M%S', 'YYYYMMDDHH24MISS'),
    ('%Y%m%d%I%M%S', 'YYYYMMDDHHMISS'),
)
)
def test_sft_to_ora(input, result):
    assert sft_to_ora(input) == result
