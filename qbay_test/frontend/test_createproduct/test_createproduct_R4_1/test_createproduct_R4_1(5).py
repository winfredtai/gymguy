from os import popen
from pathlib import Path
import subprocess

# get expected input/output file
current_folder = Path(__file__).parent

# read expected in/out
expected_in = open(current_folder.joinpath(
    'test_createproduct_R4_1(5).in'))
expected_out = open(current_folder.joinpath(
    'test_createproduct_R4_1(5).out')).read()

print(expected_out)


def test_register():
    """capsys -- object created by pytest to
    capture stdout and stderr"""

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in,
        capture_output=True,
    ).stdout.decode()
    assert output.strip() == expected_out.strip()
