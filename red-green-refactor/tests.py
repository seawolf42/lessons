# password rules
#
# must be a string
# must be at least 8 characters
# must contain at least one lower-case letter
# must contain at least one upper-case letter
# must contain at least one number

from validators import password


def test_invalid_input():
    assert not password(None)
    assert not password([])
    assert not password({})
    assert not password(1)
    assert not password(1.)


def test_length():
    assert not password('aB3defg')
    assert password('aB3defgh')


def test_contains_lower_case():
    assert not password('AB3DEFGH')
    assert password('aB3DEFGH')
    assert password('AB3DEFGh')
