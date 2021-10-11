from qbay.models import register, login, update_user, \
    update_product, create_product, User, Product


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
    assert register('user8', 'test8@test.com', '123456aA.') is True


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


    user = login('test10@test.com', '123456aA.')
    assert user is not None
    assert user.username == 'user10'

    # this account does not exist
    user = login('1222aa@test.com', '1234567aA.')
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

    assert update_user(email="test10@test.com", username="user10",
                       shipping_address="33 Evergreen Terrace",
                       postal_code="L5C 2B5") is True
    assert update_user(email="test8@test.com", username="user8",
                       shipping_address="33 Queens Cres",
                       postal_code="K7L 2H9") is True
    assert update_user(email="email", username=" ",
                       shipping_address="33 Evergreen Terrace!",
                       postal_code="83053") is False


def test_r3_2_update_user():
    '''
    Testing R3-2: Updated shipping address must be
    non empty, alphanumeric, and not contain symbols.
    '''

    assert update_user(email="test8@test.com", username="user8",
                       shipping_address="33 Evergreen Terrace",
                       postal_code="L5C 2B5") is True
    assert update_user(email="test8@test.com", username="user8",
                       shipping_address=" ",
                       postal_code="L5C 2B5") is False
    assert update_user(email="test8@test.com", username="user8",
                       shipping_address="33 Evergr33n Terrace!",
                       postal_code="L5C 2B5") is False


def test_r3_3_update_user():
    '''
    Testing R3-3: Updated postal code must be a valid
    Canadian Postal code.
    '''

    assert update_user(email="test8@test.com", username="user8",
                       shipping_address="33 Evergreen Terrace",
                       postal_code="L5C 2B5") is True
    assert update_user(email="test8@test.com", username="user8",
                       shipping_address="33 Evergreen Terrace",
                       postal_code="L55 2B88") is False


def test_r3_4_update_user():
    '''
    Testing R3-4: Updated username follows given
    requirements.
    '''

    assert update_user(email="test8@test.com", username="user8",
                       shipping_address="33 Evergreen Terrace",
                       postal_code="L5C 2B5") is True
    assert update_user(email="test8@test.com", username=" testuser4 ",
                       shipping_address="33 Evergreen Terrace",
                       postal_code="L55 2B88") is False
    assert update_user(email="test8@test.com", username="t4",
                       shipping_address="33 Evergreen Terrace",
                       postal_code="L55 2B88") is False
    assert update_user(email="test8@test.com", username=" ",
                       shipping_address="33 Evergreen Terrace",
                       postal_code="L55 2B88") is False

def test_r4_12_create_product():
    """
    Testing R4-1: The title of the product has to be alphanumeric-only,
    and space allowed only if it is not as prefix and suffix.
    Testing R4-2: The title of the product is no longer than 80 characters.
    """
    assert create_product(' wooden toys ',
                          "These wooden peg people sets are perfect "
                          "for promoting "
                          "open ended play. Your child will "
                          "love exploring and using them in many "
                          "different ways. Also "
                          "an excellent resource for early "
                          "colour recognition, counting and sorting.",
                          15.00, 'test8@test.com') is False
    assert create_product('wooden toys!!',
                          "These wooden peg people sets are perfect "
                          "for promoting open "
                          "ended play. Your child will "
                          "love exploring and using them in many "
                          "different ways. Also an "
                          "excellent resource for early "
                          "colour recognition, counting and sorting.",
                          15.00, 'test8@test.com') is False
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
                          15.00, 'test8@test.com') is False
    assert create_product('Wooden Toy and Montessori and Waldorf',
                          "These wooden peg people sets are perfect for "
                          "promoting open end"
                          "ed play. Your child will "
                          "love exploring and using them in many different "
                          "ways. Also an "
                          "excellent resource for early "
                          "colour recognition, counting and sorting.",
                          15.00, 'test8@test.com') is True


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
                          32.71, 'test8@test.com') is False
    assert create_product('Spooky Bats in a Tree', temp,
                          32.71, 'test8@test.com') is False
    assert create_product('Spooky Bats in a Tree perfect for promoting',
                          "These wooden peg people sets aru.",
                          32.71, 'test8@test.com') is False
    assert create_product('Spooky Bats in a Tree', test_string,
                          32.71, 'test8@test.com') is True


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
                          9.71, 'test8@test.com') is False
    assert create_product('Live Edge Table Live edge Vanity Live Edge',
                          testStr,
                          11111.71, 'test8@test.com') is False
    assert create_product('Live Edge Table Live edge Vanity Live Edge',
                          testStr,
                          32.71, 'test8@test.com') is True


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
                          110.75, 'test8@test.com') is True


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
                          42.00, '') is False
    assert create_product('PERSONALIZED leather hip flask', testStr,
                          42.00, 'abcdef.def@mail.com') is False
    assert create_product('PERSONALIZED leather hip flask', testStr,
                          42.00, 'test8@test.com') is True


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
                          42.00, 'test8@test.com') is False
    assert create_product('Handprint Keychain and or Footprint', testStr,
                          42.00, 'test8@test.com') is True


def test_r5_1_update_product():
    '''
    Testing R5-1: update attributes of products
      and update modified time automatically
    (will use the created product in the previous test.)
    '''
    title_existed = "Wooden Toy and Montessori and Waldorf111"
    description1 = """These wooden peg people sets are perfect for promoting 
    open ended play, Your child will love exploring and using them in many 
    different ways."""
    create_product(Title=title_existed, Description=description1, Price=15,
                   Owner_email='test8@test.com')
    description2 = """These wooden peg people sets are perfect for promoting 
    open ended play, brand new for children"""
    assert update_product(old_title=title_existed, newDescription=description1,
                          newPrice=20.0, newTitle="Wooden Toy Brand new"
                          ) is True

    assert update_product(old_title="Wooden Toy Brand new",
                          newDescription=description2, newPrice=25.0,
                          newTitle="Wooden Toy Brand new1") is True

    assert update_product(old_title="Wooden Toy Brand new1", newPrice=30.0,
                          newTitle="Wooden Toy Brand new2") is True


def test_r5_2_update_product():
    '''
    Testing R5-2: Price can be only increased but cannot be decreased
    '''
    title_existed = "Wooden Toy Brand new2"
    assert update_product(old_title=title_existed, newPrice=5.0,
                          newTitle="Wooden Toy Brand new3") is False
    assert update_product(old_title=title_existed, newPrice=35.0,
                          newTitle="Wooden Toy Brand new3") is True


def test_r5_4_update_product():
    '''
    Testing R5-4: Price has to be of range [10,10000], title has to be
    alphanumeric-only, and space allowed only if it is not as prefix and suffix.
    The description of the product can be arbitrary characters, with a minimum
    length of 20 characters and a maximum of 2000 characters. Description has
    to be longer than the product's title.
    '''
    title_existed = "Wooden Toy Brand new3"
    description1 = """The Austin vanity is proudly made in Canada. Every 
    Austin vanity is handmade to order and has a lead time of approximately 
    14 days. """
    description2 =  """The Austin vanity is proudly made in Canada. Every 
    Austin vanity is handmade to order and has a lead time of approximately 
    14 days. The Austin vanity is proudly made in Canada. Every 
    Austin vanity is handmade to order and has a lead time of approximately 
    14 days. """
    title1 = "Live edge Table"
    assert update_product(old_title=title_existed, newDescription=description1,
                          newTitle=title1, newPrice=45.0) is True
    # price must less than 10000
    assert update_product(old_title=title_existed, newDescription=description1,
                          newTitle="Live edge Table1", newPrice=20000.0
                          ) is False
    # no space at left or right
    assert update_product(old_title=title_existed, newTitle=" Live edge Table1"
                          ) is False
    assert update_product(old_title=title_existed, newTitle="Live edge Table1 "
                          ) is False
    # only alphanumeric
    assert update_product(old_title=title_existed, newTitle="Live!edge*Table1&"
                          ) is False
    # description shorter than title
    assert update_product(old_title=title_existed, newTitle="live edge Table1",
                          newDescription="abba") is False
    # description shorter than 20
    assert update_product(old_title=title_existed, newTitle="livea1",
                          newDescription="aaaaabbbbbccccc") is False
