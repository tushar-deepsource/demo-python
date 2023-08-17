def foo():
    raise RuntimeError

try:
    foo()
except Exception:  # noqa: B902  # pylint: disable=broad-except
    print("caught")
