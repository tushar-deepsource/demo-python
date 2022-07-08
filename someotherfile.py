"""Doc"""


def foo():
    """Doc"""
    print("foo")


x = 5


def bar():  # pylint: disable=disallowed-name
    """Doc"""
    print("foo")


bar()
