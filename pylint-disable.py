def foo():
    raise RuntimeError


try:
    foo()
except Exception:  # noqa # pylint: disable=broad-except
    print("caught")


def foo():
    raise RuntimeError


try:
    foo()
except Exception:  # noqa # skipcq: PYL-W0703
    print("caught")
