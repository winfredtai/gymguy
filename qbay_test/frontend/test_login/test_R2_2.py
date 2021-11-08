from pathlib import Path
import subprocess

# get expected input/output file
current_folder = Path(__file__).parent

# read expected in/out
r2_2_1_expected_in = open(current_folder.joinpath(
    'test_R2_2_1.in'))
r2_2_1_expected_out = open(current_folder.joinpath(
    'test_R2_2_1.out')).read()

r2_2_2_expected_in = open(current_folder.joinpath(
    'test_R2_2_2.in'))
r2_2_2_expected_out = open(current_folder.joinpath(
    'test_R2_2_2.out')).read()


def test_r2_2_1():
    """
    Test for Requirement 2-2
    The login function should check if the supplied inputs meet the
    same email/password requirements as above, before checking
    the database.

    Tested using output partitioning.
    Output: welcome user
    Inputs: valid email, valid password
    """

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=r2_2_1_expected_in,
        capture_output=True,
    ).stdout.decode()

    print('outputs', output)
    assert output.strip() == r2_2_1_expected_out.strip()


def test_r2_2_2():
    """
    Test for Requirement 2-2
    The login function should check if the supplied inputs meet the
    same email/password requirements as above, before checking
    the database.

    Tested using output partitioning.
    Output: login failed
    Inputs: invalid email, invalid password
    """

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=r2_2_2_expected_in,
        capture_output=True,
    ).stdout.decode()

    print('outputs', output)
    assert output.strip() == r2_2_2_expected_out.strip()
