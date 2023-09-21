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

    def some_long_method(self):
        items = (
            "attribute_1",
            "attribute_2",
            "attribute_3",
            "attribute_4",
            "attribute_5",
            "attribute_1",
            "attribute_2",
            "attribute_3",
            "attribute_4",
            "attribute_5",
        )
        return items

    @property
    @abc.abstractmethod
    def myproperty2(cls):
        pass

    @abc.abstractmethod
    def mymethod(self):
        pass
