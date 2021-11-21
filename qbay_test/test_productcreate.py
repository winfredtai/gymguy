from pathlib import Path

# get expected input/output file
from qbay.models import create_product

current_folder = Path(__file__).parent

# read expected in/out
expected_in = open(current_folder.joinpath(
    'Generic_SQLI.txt'))
Lines = expected_in.readlines()


def test_sql_productcreate():
    for i in range(len(Lines)):
        # test case 1: choosing Title as the parameter
        create_product(Lines[i],
                       "These wooden peg people sets are perfect for "
                       "promoting open end"
                       "ed play. Your child will "
                       "love exploring and using them in many different "
                       "ways. Also an "
                       "excellent resource for early "
                       "colour recognition, counting and sorting.",
                       15.00, 'test8@test.com')
        # test case 2: choosing description as the parameter
        create_product("chinatown market toys",
                       Lines[i],
                       15.00, 'test8@test.com')
        # test case 3: choosing price as the parameter
        create_product("chinatown market toys",
                       "These wooden peg people sets are perfect for "
                       "promoting open end"
                       "ed play. Your child will "
                       "love exploring and using them in many different "
                       "ways. Also an "
                       "excellent resource for early "
                       "colour recognition, counting and sorting.",
                       Lines[i], 'test8@test.com')
        # test case 4: choosing owner email as the parameter
        create_product("chinatown market toys",
                       "These wooden peg people sets are perfect for "
                       "promoting open end"
                       "ed play. Your child will "
                       "love exploring and using them in many different "
                       "ways. Also an "
                       "excellent resource for early "
                       "colour recognition, counting and sorting.",
                       15.00, Lines[i])
