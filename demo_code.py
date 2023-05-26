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

    @property
    @abc.abstractmethod
    def myproperty2(cls):
        pass

    @abc.abstractmethod
    def mymethod(self):
        pass
