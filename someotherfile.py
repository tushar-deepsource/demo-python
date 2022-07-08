"""Doc"""


def foo(): # pylint: disable=disallowed-name
    """Doc"""
    print("foo")


x = 5


def bar():
    """Doc"""
    print("foo")


bar()
