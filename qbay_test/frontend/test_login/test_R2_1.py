from pathlib import Path
import subprocess

# get expected input/output file
current_folder = Path(__file__).parent

# read expected in/out
r2_1_1_expected_in = open(current_folder.joinpath(
    'test_R2_1_1.in'))
r2_1_1_expected_out = open(current_folder.joinpath(
    'test_R2_1_1.out')).read()

r2_1_2_expected_in = open(current_folder.joinpath(
    'test_R2_1_2.in'))
r2_1_2_expected_out = open(current_folder.joinpath(
    'test_R2_1_2.out')).read()

r2_1_3_expected_in = open(current_folder.joinpath(
    'test_R2_1_3.in'))
r2_1_3_expected_out = open(current_folder.joinpath(
    'test_R2_1_3.out')).read()

r2_1_4_expected_in = open(current_folder.joinpath(
    'test_R2_1_4.in'))
r2_1_4_expected_out = open(current_folder.joinpath(
    'test_R2_1_4.out')).read()


def test_r2_1_1():
    """
    Test for Requirement 2-1
    A user can log in using her/his email address and the
    password.

    Tested using input partitioning.
    Inputs: valid email, valid password
    Output: welcome user
    """

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=r2_1_1_expected_in,
        capture_output=True,
    ).stdout.replace(b'\r\n', b'\n').decode()

    print('outputs', output)
    assert output.strip() == r2_1_1_expected_out.strip()


def test_r2_1_2():
    """
    Test for Requirement 2-1
    A user can log in using her/his email address and the
    password.

    Tested using input partitioning.
    Inputs: invalid email, valid password
    """

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=r2_1_2_expected_in,
        capture_output=True,
    ).stdout.replace(b'\r\n', b'\n').decode()

    print('outputs', output)
    assert output.strip() == r2_1_2_expected_out.strip()


def test_r2_1_3():
    """
    Test for Requirement 2-1
    A user can log in using her/his email address and the
    password.

    Tested using input partitioning.
    Inputs: valid email, invalid password
    """

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=r2_1_3_expected_in,
        capture_output=True,
    ).stdout.replace(b'\r\n', b'\n').decode()

    print('outputs', output)
    assert output.strip() == r2_1_3_expected_out.strip()


def test_r2_1_4():
    """
    Test for Requirement 2-1
    A user can log in using her/his email address and the
    password.

    Tested using input partitioning.
    Inputs: invalid email, invalid password
    """

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=r2_1_4_expected_in,
        capture_output=True,
    ).stdout.replace(b'\r\n', b'\n').decode()
    print('outputs', output)
    assert output.strip() == r2_1_4_expected_out.strip()
