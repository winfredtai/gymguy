from os import popen
from pathlib import Path
import subprocess

# get expected input/output file
current_folder = Path(__file__).parent


# read expected in/out
expected_in = open(current_folder.joinpath(
    'test_R6_5.in'))
expected_out = open(current_folder.joinpath(
    'test_R6_5.out')).read()

print(expected_out)


def test_place_order_5():
    """
    This is for testing a sold product can be shown on
    the owner's user interface.

    User(purchase):test10@test.com

    Product(purchased):
    Wooden Toy and Montessori and
    Waldosajdnjdnajndjakndlkandlkandklanlkdnlkandlkan1

    User(Owner):test1@test.com

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
