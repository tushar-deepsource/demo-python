"""Type tests"""
from typing import TypeAlias

def foo() -> None:
    return 42

def bar() -> int:
    return 'abc'

def baz() -> str:
    print('stuff')

spam: TypeAlias = int()
