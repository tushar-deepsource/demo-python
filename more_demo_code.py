import urllib.parse
import random

from urllib.parse import urlparse

# import time
# import timeit

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

logo = (
    " __   ___  ___  __   __   __        __   __   ___ \n"
    "|  \ |__  |__  |__) /__` /  \ |  | |__) /  ` |__  \n"
    "|__/ |___ |___ |    .__/ \__/ \__/ |  \ \__, |___ \n"
)


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
    
all_good_values = True


url = urlparse("https://google.com/?q=deepsource+python")
if url.hostname == "google.com" or url.hostname == "github.com":
    print("OAuth provider detected")

if urllib.parse.ParseResult == type(url):
    print(url.scheme)

evens = set([num for num in range(10) if num % 2 == 0])
assert 8 in evens