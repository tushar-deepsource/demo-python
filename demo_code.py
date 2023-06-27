"""Doc"""
import abc


def f():
    """
    x
    y

    z
    """
    print(_, foo)


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

def foo():
    """
    This docstring is 80 characters long, normally flake8 would raise on this.
    """

def bar():
    """
    This docstring is 90 characters long, still no issue as we set the max line length to 100.
    """


def baz():
    """
    This docstring is 105 characters long, now that is an issue, this is longer than max line length so raise here.
    """
