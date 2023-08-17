def foo():
    raise RuntimeError

try:
    foo()
except Exception: # noqa: B902 # pylint: disable=broad-except
    print("caught")

try:
    foo()
except Exception: # noqa: B902 # skipcq: PYL-W0703
    print("caught")

try:
    foo()
except Exception: # noqa: B902 # pylint: disable
    print("caught")

try:
    foo()
except Exception: # noqa: B902 # skipcq
    print("caught")

class Foo:
    class RelatedModel(Model):  # pylint: disable=unused-variable # skipcq: PTC-W0065
        """Something"""
        def foo(self):
            print("foo")

    class AnotherModel(Model):  # pylint: disable=unused-variable # skipcq: PTC-W0065
        """Something"""
        def bar(self):
            print("bar")
