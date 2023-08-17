def foo():
    raise RuntimeError


try:
    foo()
except Exception:  # noqa: B902 # pylint: disable=broad-except
    print("caught")


def foo():
    raise RuntimeError


try:
    foo()
except Exception:  # noqa: B902 # skipcq: PYL-W0703
    print("caught")


def foo():
    raise RuntimeError


try:
    foo()
except Exception:  # noqa: B902 # pylint: disable
    print("caught")


def foo():
    raise RuntimeError


try:
    foo()
except Exception:  # noqa: B902 # skipcq
    print("caught")
