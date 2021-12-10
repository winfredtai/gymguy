from pathlib import Path

# get expected input/output file
from qbay.models import purchase_product

current_folder = Path(__file__).parent

# read expected in/out
expected_in = open(current_folder.joinpath(
    'Generic_SQLI.txt'))
Lines = expected_in.readlines()


def test_sql_placeorder():
    for i in range(len(Lines)):
        # test case 1: choosing user email as the parameter
        purchase_product(Lines[i], 'Wooden Toy and Montessori and Waldorf')
        # test case 2: choosing product title as the parameter
        purchase_product("test5@test.com", Lines[i])
