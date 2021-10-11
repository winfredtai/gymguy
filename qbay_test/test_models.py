from qbay.models import register, login, update_user, updateProductTittle, updateProductDescription, updateProductPrice
from qbay_test.conftest import pytest_sessionstart

pytest_sessionstart()


def test_r1_1_user_register():
    '''
    Testing R1-1: If the email or password (or both) is empty, the operation
    failed.
    '''

    assert register('user1', 'test0@test.com', '') is False
    assert register('user1', '', '123456aA.') is False
    assert register('user1', '', '') is False
    assert register('user1', 'test1@test.com', '123456aA.') is True


def test_r1_2_user_register():
    '''
     Testing R1-1: If the email is the primary key, the operation
     success. (Specified in User())
     '''
    assert register('userp1', 'testp1@test.com', '123456aA.') is True


def test_r1_3_user_register():
    '''
    Testing R1-3: If the email does not follow RFC5322, the operation
    failed.
    '''
    assert register('user2', 'test2@test.com', '123456aA.') is True
    assert register('user1', 'aaa@w2@', '123456aA.') is False


def test_r1_4_user_register():
    '''
    Testing R1-4: If the password does not meet the complexity, the operation
    failed. (minimum length 6, at least one upper case, at least one lower
    case, and at least one special character.)
    '''
    assert register('user3', 'test3@test.com', '123456aA.') is True
    assert register('user1', 'test0@test.com', '1234') is False
    assert register('user1', 'test0@test.com', '12aA.') is False
    assert register('user1', 'test0@test.com', '123456') is False
    assert register('user1', 'test0@test.com', '123456a.') is False
    assert register('user1', 'test0@test.com', '123456A.') is False
    assert register('user1', 'test0@test.com', '12346aa.') is False
    assert register('user1', 'test0@test.com', '12346AA.') is False
    assert register('user1', 'test0@test.com', '12346aA') is False


def test_r1_5_user_register():
    '''
    Testing R1-5: If the username does not meet the requirement, the operation
    failed. (User name has to be non-empty, alphanumeric-only, and space
    allowed only if it is not as the prefix or suffix.)
    '''
    assert register('user4', 'test4@test.com', '123456aA.') is True
    assert register('', 'test0@test.com', '123456aA.') is False
    assert register('user1.', 'test0@test.com', '123456aA.') is False
    assert register('user1 ', 'test0@test.com', '123456aA.') is False
    assert register(' user1', 'test0@test.com', '123456aA.') is False
    assert register('use r1', 'test11@test.com', '123456aA.') is True


def test_r1_6_user_register():
    '''
    Testing R1-6: If the username does not meet the requirement, the operation
    failed. (User name has to be longer than 2 characters and less than 20
    characters.)
    '''
    assert register('user5', 'test5@test.com', '123456aA.') is True
    assert register('us', 'test0@test.com', '123456aA.') is False
    assert register('aaaaabbbbbcccccddddd', 'test0@test.com',
                    '123456aA.') is False


def test_r1_7_user_register():
    '''
    Testing R1-7: If the email has been used, the operation failed.
    '''

    assert register('user6', 'test6@test.com', '123456aA.') is True
    assert register('user7', 'test7@test.com', '123456aA.') is True
    assert register('user009', 'test7@test.com', '123456') is False


def test_r1_8_user_register():
    '''
    Testing R1-8: If Shipping address is empty at the time of registration,
    the operation success.
    '''
    assert register('user8', 'tes8@test.com', '123456aA.') is True


def test_r1_9_user_register():
    '''
    Testing R1-8: If Postal code is empty at the time of registration,
    the operation success.
    '''
    assert register('user9', 'test9@test.com', '123456aA.') is True


def test_r1_10_user_register():
    '''
    Testing R1-8: If  Balance should be initialized as 100 at the time of
    registration, the operation success.
    '''
    assert register('user10', 'test10@test.com', '123456aA.') is True


def test_r2_1_login():
    '''
    Testing R2-1: A user can log in using her/his email address
      and the password.
    (will be tested after the previous test, so we already have u0,
      u1 in database)
    '''

    user = login('test0@test.com', 123456)
    assert user is not None
    assert user.username == 'u0'

    user = login('test0@test.com', 1234567)
    assert user is None


def test_r2_2_login():
    '''
    Testing R2-2: A user's inputs match the requirements.
    '''

    user = login('he', 'hello')
    assert user is None

    user = login('he.hey', 'HELLO$')
    assert user is None


def test_r3_1_update_user():
    '''
    Testing R3-1: A user can update their username,
    shipping address and postal code.
    '''

    assert update_user(email="testuser1@gmail.com", username="testuser1",
                       shipping_address="33 Evergreen Terrace",
                       postal_code="L5C 2B5") is True
    assert update_user(email="email", username=" ",
                       shipping_address="33 Evergreen Terrace!",
                       postal_code="83053") is False


def test_r3_2_update_user():
    '''
    Testing R3-2: Updated shipping address must be
    non empty, alphanumeric, and not contain symbols.
    '''

    assert update_user(email="testuser2@gmail.com", username="testuser2",
                       shipping_address="33 Evergreen Terrace",
                       postal_code="L5C 2B5") is True
    assert update_user(email="testuser2@gmail.com", username="testuser2",
                       shipping_address=" ",
                       postal_code="L5C 2B5") is False
    assert update_user(email="testuser2@gmail.com", username="testuser2",
                       shipping_address="33 Evergr33n Terrace!",
                       postal_code="L5C 2B5") is False


def test_r3_3_update_user():
    '''
    Testing R3-3: Updated postal code must be a valid
    Canadian Postal code.
    '''

    assert update_user(email="testuser3@gmail.com", username="testuser3",
                       shipping_address="33 Evergreen Terrace",
                       postal_code="L5C 2B5") is True
    assert update_user(email="testuser3@gmail.com", username="testuser3",
                       shipping_address="33 Evergreen Terrace",
                       postal_code="L55 2B88") is False


def test_r3_4_update_user():
    '''
    Testing R3-4: Updated username follows given
    requirements.
    '''

    assert update_user(email="testuser4@gmail.com", username="testuser4",
                       shipping_address="33 Evergreen Terrace",
                       postal_code="L5C 2B5") is True
    assert update_user(email="testuser4@gmail.com", username=" testuser4 ",
                       shipping_address="33 Evergreen Terrace",
                       postal_code="L55 2B88") is False
    assert update_user(email="testuser4@gmail.com", username="t4",
                       shipping_address="33 Evergreen Terrace",
                       postal_code="L55 2B88") is False
    assert update_user(email="testuser4@gmail.com", username=" ",
                       shipping_address="33 Evergreen Terrace",
                       postal_code="L55 2B88") is False


def test_r4_12_create_product():
    '''
    Testing R4-1: The title of the product has to be alphanumeric-only,
    and space allowed only if it is not as prefix and suffix.
    Testing R4-2: The title of the product is no longer than 80 characters.
    '''
    assert create_product(' wooden toys ',
                          "These wooden peg people sets are perfect "
                          "for promoting "
                          "open ended play. Your child will "
                          "love exploring and using them in many "
                          "different ways. Also "
                          "an excellent resource for early "
                          "colour recognition, counting and sorting.",
                          15.00, '2021-10-15', 'test0@test.com') is False
    assert create_product('wooden toys!!',
                          "These wooden peg people sets are perfect "
                          "for promoting open "
                          "ended play. Your child will "
                          "love exploring and using them in many "
                          "different ways. Also an "
                          "excellent resource for early "
                          "colour recognition, counting and sorting.",
                          15.00, '2021-10-15', 'test0@test.com') is False
    assert create_product('sdfghjklwertyuioasdfghjklwertyuiosdfghjksdfgh'
                          'kledfgthjklertyu'
                          'iosdfghyjukldfghjksdfgh',
                          "These wooden peg people sets are perfect for "
                          "promoting open en"
                          "ded play. Your child will "
                          "love exploring and using them in many "
                          "different ways. Also an "
                          "excellent resource for early "
                          "colour recognition, counting and sorting.",
                          15.00, '2021-10-15', 'test0@test.com') is False
    assert create_product('Wooden Toy and Montessori and Waldorf',
                          "These wooden peg people sets are perfect for "
                          "promoting open end"
                          "ed play. Your child will "
                          "love exploring and using them in many different "
                          "ways. Also an "
                          "excellent resource for early "
                          "colour recognition, counting and sorting.",
                          15.00, '2021-10-15', 'test0@test.com') is True


def test_r4_34_create_product():
    '''
    Testing R4-3: The description of the product can be arbitrary
    characters,
    with a minimum length of 20 characters and a maximum of 2000
    characters.
    Testing R4-4: Description has to be longer than the product's title.
    '''

    test_string = "Halloween-themed wooden Spooky Tree and bats playset " \
                  "for small world " \
                  "play and seasonal decor. " \
                  "Handmade from Maple Hardwood, Each piece is cut by " \
                  "hand, sanded smooth" \
                  ", painted, and sealed for " \
                  "durability with non-toxic acrylics, stains, and sealer. "
    temp = ''
    for i in range(11):
        temp += test_string
    assert create_product('Spooky Bats',
                          "These wooden peg",
                          32.71, '2022-10-15', 'test0@test.com') is False
    assert create_product('Spooky Bats in a Tree', temp,
                          32.71, '2022-10-15', 'test0@test.com') is False
    assert create_product('Spooky Bats in a Tree perfect for promoting',
                          "These wooden peg people sets aru.",
                          32.71, '2022-10-15', 'test0@test.com') is False
    assert create_product('Spooky Bats in a Tree', test_string,
                          32.71, '2022-10-15', 'test0@test.com') is True


def test_r4_5_create_product():
    '''
    Testing R4-5: Price has to be of range [10, 10000].
    '''
    testStr = "The Austin vanity is proudly made in Canada. Every " \
              "Austin vanity is " \
              "handmade to order and has a lead " \
              "time of approximately 14 days. "

    assert create_product('Live Edge Table Live edge Vanity Live Edge',
                          testStr,
                          9.71, '2022-11-15', 'test0@test.com') is False
    assert create_product('Live Edge Table Live edge Vanity Live Edge',
                          testStr,
                          11111.71, '2022-11-15', 'test0@test.com') is False
    assert create_product('Live Edge Table Live edge Vanity Live Edge',
                          testStr,
                          32.71, '2022-11-15', 'test0@test.com') is True


def test_r4_6_create_product():
    '''
    Testing R4-6: last_modified_date must be after 2021-01-02 and
    before 2025-01-02.
    '''
    testStr = "SASKIA burgundy leather purse - designed in " \
              "collaboration with DJ, " \
              "activist and fashion icon Honey " \
              "Dijon as part of the exclusive Etsy Creator Collab. "

    assert create_product('Honey Dijon Creator Collab', testStr,
                          110.75, '2021-01-01', 'test0@test.com') is False
    assert create_product('Honey Dijon Creator Collab', testStr,
                          110.75, '2025-02-02', 'test0@test.com') is False
    assert create_product('Honey Dijon Creator Collab', testStr,
                          110.75, '2022-12-15', 'test0@test.com') is True


def test_r4_7_create_product():
    '''
    Testing R4-7: owner_email cannot be empty. The owner of
    the corresponding
    product must exist in the database.
    '''
    testStr = "Our 6oz stainless steel flask is handwrapped " \
              "using the highest " \
              "quality, North American sourced " \
              "leather. Each leather wrap is hand stitched using " \
              "a premium waxed " \
              "thread in a variety of color options. "

    assert create_product('PERSONALIZED leather hip flask', testStr,
                          42.00, '2023-12-15', '') is False
    assert create_product('PERSONALIZED leather hip flask', testStr,
                          42.00, '2023-12-15', 'abcdef.def@mail.com') is False
    assert create_product('PERSONALIZED leather hip flask', testStr,
                          42.00, '2023-12-15', 'test0@test.com') is True


def test_r4_8_create_product():
    '''
    Testing R4-8: A user cannot create products that have the same title.
    '''
    testStr = "Our 6oz stainless steel flask is handwrapped " \
              "using the highest " \
              "quality, North American sourced " \
              "leather. Each leather wrap is hand stitched " \
              "using a premium waxed " \
              "thread in a variety of color options. "

    assert create_product('PERSONALIZED leather hip flask', testStr,
                          42.00, '2023-12-15', '') is False
    assert create_product('Handprint Keychain and or Footprint', testStr,
                          42.00, '2023-12-15', 'test0@test.com') is True


def test_r5_1_productUpdate():
    '''
    Testing R3-1: update attributes of products
      and update modified time automatically
    (will use the created product in the previous test.)
    '''

    assert updateProductTittle(ID = 1, newTittle = "product") is True
    assert updateProductDescription(ID = 1, newDescription = "product") is True
    assert updateProductPrice(ID = 1, newPrice = 13) is True


def test_r5_2_productUpdate():
    '''
    Testing R3-2: ID, tittle, description cannot be empty
    (will use the created product in the previous test.)
    '''

    assert updateProductTittle(ID = None, newTittle = "product") is False
    assert updateProductDescription(ID = None, newDescription = "") is False
    assert updateProductPrice(ID = None, newPrice = 13) is False
    assert updateProductTittle(ID = 1, newTittle = "") is False
    assert updateProductDescription(ID = 1, newDescription = "") is False
    assert updateProductPrice(ID = 1, newPrice = None) is False
