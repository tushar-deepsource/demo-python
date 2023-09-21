"""Doc"""
import abc


def f():
    """
    x
    y

    z
    """


class MyAbstractClass:
    """Test"""

    @abc.abstractproperty
    def myproperty(self):
        pass

    def some_long_method(
        attribute_1: str | None = None,
        attribute_2: str | None = None,
        attribute_3: str | None = None,
        attribute_4: str | None = None,
        attribute_5: str | None = None,
    ):
        pass
    
    @property
    @abc.abstractmethod
    def myproperty2(cls):
        pass

    @abc.abstractmethod
    def mymethod(self):
        pass
