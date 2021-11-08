from os import popen
from pathlib import Path
import subprocess

# get expected input/output file
current_folder = Path(__file__).parent


# read expected in/out
r5_1_expected_in = open(current_folder.joinpath('test_R5-1.in'))
r5_1_expected_out = open(current_folder.joinpath('test_R5-1.out')).read()

r5_2_expected_in = open(current_folder.joinpath('test_R5-2.in'))
r5_2_expected_out = open(current_folder.joinpath('test_R5-2.out')).read()

r5_3_expected_in = open(current_folder.joinpath('test_R5-3.in'))
r5_3_expected_out = open(current_folder.joinpath('test_R5-3.out')).read()

r5_4_expected_in = open(current_folder.joinpath('test_R5-4.in'))
r5_4_expected_out = open(current_folder.joinpath('test_R5-4.out')).read()


def test_r5_1():
    """
    created user attribute:
        user name:abc
        user email:123@gmail.com
        user password:Abc123!@#
    created product attribute:
        product title:a new product
        product description: this is a new product
        product price:11
    capsys -- object created by pytest to
    capture stdout and stderr
    """

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=r5_1_expected_in,
        capture_output=True,
    ).stdout.replace(b'\r\n', b'\n').decode()

    print('outputs', output)
    assert output.strip() == r5_1_expected_out.strip()


def test_r5_2():
    """
    boundary testing
    capsys -- object created by pytest to
    capture stdout and stderr
    """

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=r5_2_expected_in,
        capture_output=True,
    ).stdout.replace(b'\r\n', b'\n').decode()

    print('outputs', output)
    assert output.strip() == r5_2_expected_out.strip()


def test_r5_3():
    """
    exhaustive output testing
    capsys -- object created by pytest to
    capture stdout and stderr
    """

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=r5_3_expected_in,
        capture_output=True,
    ).stdout.replace(b'\r\n', b'\n').decode()

    print('outputs', output)
    assert output.strip() == r5_3_expected_out.strip()


def test_r5_4():
    """
    input partition testing
    capsys -- object created by pytest to
    capture stdout and stderr
    """

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=r5_4_expected_in,
        capture_output=True,
    ).stdout.replace(b'\r\n', b'\n').decode()

    print('outputs', output)
    assert output.strip() == r5_4_expected_out.strip()
