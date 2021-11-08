from pathlib import Path
import subprocess

# get expected input/output file
current_folder = Path(__file__).parent

# read expected in/out
r3_2_1_expected_in = open(current_folder.joinpath(
    'test_R3_2_1.in'))
r3_2_1_expected_out = open(current_folder.joinpath(
    'test_R3_2_1.out')).read()

r3_2_2_expected_in = open(current_folder.joinpath(
    'test_R3_2_2.in'))
r3_2_2_expected_out = open(current_folder.joinpath(
    'test_R3_2_2.out')).read()

r3_2_3_expected_in = open(current_folder.joinpath(
    'test_R3_2_3.in'))
r3_2_3_expected_out = open(current_folder.joinpath(
    'test_R3_2_3.out')).read()


def test_r3_2_1():
    """
    Test for Requirement 3-2
    Shipping_address should be non-empty, alphanumeric-only, and
    no special characters such as !.

    Tested using input partitioning.
    Input: non-empty, alphanumeric, no special characters
    """

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=r3_2_1_expected_in,
        capture_output=True,
    ).stdout.decode()

    print('outputs', output)
    assert output.strip() == r3_2_1_expected_out.strip()


def test_r3_2_2():
    """
    Test for Requirement 3-2
    Shipping_address should be non-empty, alphanumeric-only, and
    no special characters such as !.

    Tested using input partitioning.
    Input: empty string
    """

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=r3_2_2_expected_in,
        capture_output=True,
    ).stdout.decode()

    print('outputs', output)
    assert output.strip() == r3_2_2_expected_out.strip()


def test_r3_2_3():
    """
    Test for Requirement 3-2
    Shipping_address should be non-empty, alphanumeric-only, and
    no special characters such as !.

    Tested using input partitioning.
    Input: non-empty, alphanumeric, has special characters
    """

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=r3_2_3_expected_in,
        capture_output=True,
    ).stdout.decode()

    print('outputs', output)
    assert output.strip() == r3_2_3_expected_out.strip()
