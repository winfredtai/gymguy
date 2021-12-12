from pathlib import Path
import subprocess

# get expected input/output file
current_folder = Path(__file__).parent

# read expected in/out
r3_1_expected_in = open(current_folder.joinpath(
    'test_R3_1.in'))
r3_1_expected_out = open(current_folder.joinpath(
    'test_R3_1.out')).read()


def test_r3_1():
    """
    Test for Requirement 3-1
    A user is only able to update his/her user name,
    shipping_address, and postal_code.

    Tested using functionality coverage.
    """

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=r3_1_expected_in,
        capture_output=True,
    ).stdout.replace(b'\r\n', b'\n').decode()

    print('outputs', output)
    assert output.strip() == r3_1_expected_out.strip()
