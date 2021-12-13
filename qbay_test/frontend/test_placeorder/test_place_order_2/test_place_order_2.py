from os import popen
from pathlib import Path
import subprocess

# get expected input/output file
current_folder = Path(__file__).parent


# read expected in/out
expected_in = open(current_folder.joinpath(
    'test_R6_2.in'))
expected_out = open(current_folder.joinpath(
    'test_R6_2.out')).read()

print(expected_out)


def test_place_order_2():
    """
    testR6_2 is for testing a user cannot place an order for his/her products.

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
