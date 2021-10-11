from qbay.models import register, login, update_user


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
