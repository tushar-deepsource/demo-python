"""Doc"""
import abc


class Base:
    """Doc"""

    def __init__(self):
        self.base = 1


class BaseOne:
    """Doc"""

    def __init__(self):
        self.base_one = 2


class Child(Base, BaseOne, Base, BaseOne):
    """Some Child class"""


class ChildOne(Base, BaseOne, Base, BaseOne, abc.ABC, abc.ABCMeta, abc.ABCMeta):
    """Class with duplicate bases"""
