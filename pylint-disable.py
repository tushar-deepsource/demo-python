def foo():
    raise RuntimeError


try:
    foo()
except Exception:  # pylint: disable=broad-except # noqa
    print("caught")
