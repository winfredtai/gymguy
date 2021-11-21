from pathlib import Path

# get expected input/output file
from qbay.models import register

current_folder = Path(__file__).parent

# read expected in/out
expected_in = open(current_folder.joinpath(
    'Generic_SQLI.txt'))
lines = expected_in.readlines()


def test_sql_register():
    for i in range(len(lines)):
        # test case 1: choosing name as the injection parameter
        register(lines[i], 'test1@test.com', '123456aA.')

        # test case 2: choosing email as the injection parameter
        register('user1', lines[i], '123456aA.')

        # test case 3: choosing password as the injection parameter
        register('user1', 'test1@test.com', lines[i])
