from abc import ABCMeta


def find_book(books, book_name):
    for book in books:
        if book == book_name:
            print("Found")
    else:
        print("Not found")


if 5 is 5:
    print("It works! Sometimes!")

if (a := 3 / 2) > 1:
    print("floating point math")


class SomeABC(metaclass=ABCMeta):
    ...
