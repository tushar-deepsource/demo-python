import unittest.mock
import random

import unittest

# import time
# import unittest


value = input("> ")
if value == "red" or value == "blue":
    print("Colors")

items = ["23", "spam", "715", "foo"]
items.append("bar")

numbers = set([item for item in items if item.isdigit()])

good_digits = {1, 3, 7}
good_digits.add(9)
good_digits.add(15)

# Needed to get past the proxy
params = {"HOST": "127.0.0.1", "PORT": 8000}
params["User-agent"] = "Mozilla/5.0"


def is_bad(item):
    return "bad" in item


def func():
    for item in items:
        if is_bad(item):
            return True

    return False


for item in items:
    if is_bad(item):
        all_good_values = False
else:
    all_good_values = True
