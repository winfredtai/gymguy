from qbay.models import register, login, update_user


def test_r1_7_user_register():
    '''
    Testing R1-7: If the email has been used, the operation failed.
    '''

    assert register('u0', 'test0@test.com', '123456') is True
    assert register('u0', 'test1@test.com', '123456') is True
    assert register('u1', 'test0@test.com', '123456') is False


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
