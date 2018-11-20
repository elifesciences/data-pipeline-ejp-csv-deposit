import io, json, pytest
from .. import ejpcsv2json as ecj

simplest_fixture = '''"Query: POA Received"
"Generated on November 18, 2018"
 
"poa_m_ms_id","poa_m_ms_no","poa_r_received_dt","poa_r_receipt_dt2"
"38546","27706","2017-04-11 15:38:47.637","2017-06-01 03:31:21.817"
"42025","30325","2017-07-11 08:08:57.670","2017-07-26 05:14:54.213"'''

time_frozen_at = '2018-11-01 23:59:59'

@pytest.mark.freeze_time(time_frozen_at)
def test_standard_parse():
    buffer = io.StringIO()
    writer = lambda x: buffer.write(str(x) + "\n")
    ecj.main(io.StringIO(simplest_fixture), writer)
    json_lines = buffer.getvalue().splitlines()
    actual = list(map(json.loads, json_lines))
    expected = [
        {'poa_m_ms_id': '38546', 'poa_m_ms_no': '27706', 'poa_r_received_dt': '2017-04-11 15:38:47.637', 'poa_r_receipt_dt2': '2017-06-01 03:31:21.817', 'generated_date': '2018-11-18', 'imported_timestamp': '2018-11-01T23:59:59Z'},
        {'poa_m_ms_id': '42025', 'poa_m_ms_no': '30325', 'poa_r_received_dt': '2017-07-11 08:08:57.670', 'poa_r_receipt_dt2': '2017-07-26 05:14:54.213', 'generated_date': '2018-11-18', 'imported_timestamp': '2018-11-01T23:59:59Z'}]
    assert expected == actual
