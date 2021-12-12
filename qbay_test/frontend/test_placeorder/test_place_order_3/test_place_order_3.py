from os import popen
from pathlib import Path
import subprocess

# get expected input/output file
current_folder = Path(__file__).parent


# read expected in/out
expected_in = open(current_folder.joinpath(
    'test_R6_3.in'))
expected_out = open(current_folder.joinpath(
    'test_R6_3.out')).read()

print(expected_out)


def test_place_order_3():
    """
    testR6_3 is for testing a user cannot place an order that costs more than
    his/her balance.

    capsys -- object created by pytest to
    capture stdout and stderr
    """

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in,
        capture_output=True,
    ).stdout.replace(b'\r\n', b'\n').decode()

    print('outputs', output)
    assert output.strip() == expected_out.strip()
