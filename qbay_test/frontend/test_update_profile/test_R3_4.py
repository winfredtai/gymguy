from pathlib import Path
import subprocess

# get expected input/output file
current_folder = Path(__file__).parent

# read expected in/out
r3_4_1_expected_in = open(current_folder.joinpath(
    'test_R3_4_1.in'))
r3_4_1_expected_out = open(current_folder.joinpath(
    'test_R3_4_1.out')).read()

r3_4_2_expected_in = open(current_folder.joinpath(
    'test_R3_4_2.in'))
r3_4_2_expected_out = open(current_folder.joinpath(
    'test_R3_4_2.out')).read()

r3_4_3_expected_in = open(current_folder.joinpath(
    'test_R3_4_3.in'))
r3_4_3_expected_out = open(current_folder.joinpath(
    'test_R3_4_3.out')).read()

r3_4_4_expected_in = open(current_folder.joinpath(
    'test_R3_4_4.in'))
r3_4_4_expected_out = open(current_folder.joinpath(
    'test_R3_4_4.out')).read()


def test_r3_4_1():
    """
    Test for Requirement 3-4
    User name follows the requirements above.

    Tested using input partitioning.
    Input: valid username
    """

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=r3_4_1_expected_in,
        capture_output=True,
    ).stdout.replace(b'\r\n', b'\n').decode()

    print('outputs', output)
    assert output.strip() == r3_4_1_expected_out.strip()


def test_r3_4_2():
    """
    Test for Requirement 3-4
    User name follows the requirements above.

    Tested using input partitioning.
    Input: username is not matching word criteria
    """

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=r3_4_2_expected_in,
        capture_output=True,
    ).stdout.replace(b'\r\n', b'\n').decode()

    print('outputs', output)
    assert output.strip() == r3_4_2_expected_out.strip()


def test_r3_4_3():
    """
    Test for Requirement 3-4
    User name follows the requirements above.

    Tested using input partitioning.
    Input: username is less than 2 characters
    """

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=r3_4_3_expected_in,
        capture_output=True,
    ).stdout.replace(b'\r\n', b'\n').decode()

    print('outputs', output)
    assert output.strip() == r3_4_3_expected_out.strip()


def test_r3_4_4():
    """
    Test for Requirement 3-4
    User name follows the requirements above.

    Tested using input partitioning.
    Input: username is more than 20 characters
    """

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=r3_4_4_expected_in,
        capture_output=True,
    ).stdout.replace(b'\r\n', b'\n').decode()

    print('outputs', output)
    assert output.strip() == r3_4_4_expected_out.strip()
