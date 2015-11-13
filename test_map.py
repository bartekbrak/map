import subprocess
import tempfile


def test_getting_same_results_on_empty_map_file():
    echo_payload = 'line1\nline2'
    with tempfile.NamedTemporaryFile() as nomap:
        nomap.write(b'{}')
        nomap.flush()
        echo_out = subprocess.check_output(
            'echo "%s" | python3 map.py %s' % (echo_payload, nomap.name),
            shell=True,
            universal_newlines=True
        )
        assert echo_out == echo_payload + '\n'


def test_change_using_map():
    with tempfile.NamedTemporaryFile() as nomap:
        nomap.write(b'{"line1": "changed1"}')
        nomap.flush()
        echo_out = subprocess.check_output(
            'echo "line1\nline2" | python3 map.py %s' % nomap.name,
            shell=True,
            universal_newlines=True
        )
        assert echo_out == 'changed1\nline2\n'

def test_error_on_no_map():
    echo_out = subprocess.check_output(
        'echo "line1\nline2" | python3 map.py; exit 0',
        shell=True,
        universal_newlines=True,
        stderr=subprocess.STDOUT
    )
    assert echo_out == 'Provide a map file.\n'
