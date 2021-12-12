from pathlib import Path
import subprocess

# get expected input/output file
current_folder = Path(__file__).parent

# read expected in/out
r3_3_1_expected_in = open(current_folder.joinpath(
    'test_R3_3_1.in'))
r3_3_1_expected_out = open(current_folder.joinpath(
    'test_R3_3_1.out')).read()

r3_3_2_expected_in = open(current_folder.joinpath(
    'test_R3_3_2.in'))
r3_3_2_expected_out = open(current_folder.joinpath(
    'test_R3_3_2.out')).read()


def test_r3_2_1():
    """
    Test for Requirement 3-3
    Postal code has to be a valid Canadian postal code.

    Tested using output partitioning.
    Output: profile update succeed
    Input: valid postal code
    """

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=r3_3_1_expected_in,
        capture_output=True,
    ).stdout.replace(b'\r\n', b'\n').decode()

    print('outputs', output)
    assert output.strip() == r3_3_1_expected_out.strip()


def test_r3_3_2():
    """
    Test for Requirement 3-3
    Postal code has to be a valid Canadian postal code.

    Tested using output partitioning.
    Output: profile update succeed
    Input: valid postal code
    """

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=r3_3_2_expected_in,
        capture_output=True,
    ).stdout.replace(b'\r\n', b'\n').decode()

    print('outputs', output)
    assert output.strip() == r3_3_2_expected_out.strip()
