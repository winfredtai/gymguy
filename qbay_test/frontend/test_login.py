from os import popen
from pathlib import Path
import subprocess

# get expected input/output file
current_folder = Path(__file__).parent


# read expected in/out
r2_1_expected_in = open(current_folder.joinpath(
 'test_R2-1.in'))
r2_1_expected_out = open(current_folder.joinpath(
 'test_R2-1.out')).read()

r2_2_expected_in = open(current_folder.joinpath(
 'test_R2-2.in'))
r2_2_expected_out = open(current_folder.joinpath(
 'test_R2-2.out')).read()


def test_r2_1():
    """capsys -- object created by pytest to
    capture stdout and stderr"""

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=r2_1_expected_in,
        capture_output=True,
    ).stdout.decode()

    print('outputs', output)
    assert output.strip() == r2_1_expected_out.strip()

def test_r2_2():
    """capsys -- object created by pytest to
    capture stdout and stderr"""

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=r2_2_expected_in,
        capture_output=True,
    ).stdout.decode()

    print('outputs', output)
    assert output.strip() == r2_2_expected_out.strip()