from os import popen
from pathlib import Path
import subprocess

# get expected input/output file
current_folder = Path(__file__).parent

# read expected in/out
expected_in = open(current_folder.joinpath(
    'test_createproduct_R4_1(2).in'))
expected_out = open(current_folder.joinpath(
    'test_createproduct_R4_1(2).out')).read()


def test_createproduct_R4_1_2():
    """capsys -- object created by pytest to
    capture stdout and stderr"""

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in,
        capture_output=True,
    ).stdout.replace(b'\r\n', b'\n').decode()
    assert output.strip() == expected_out.strip()
