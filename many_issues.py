"""Doc"""
import datetime

from django.http import HttpResponse
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET", "POST"])  # Sensitive
def current_datetime(request):
    """Doc"""
    now = datetime.datetime.now()
    html = "<html><body>It is %s.</body></html>" % now
    return HttpResponse(html)


from utils import get_next, render_to_frontend, render_bg


class Orange:
    """Represents the fruit orange."""

    orange = "#FFA500"

    # Other class implementations

    def get_orange(self):
        """Doc"""
        return self.orange


def render():
    """Doc"""
    fruit = Orange()
    render_to_frontend(fruit.orange)  # Rendering a color, but one can get confused with the fruit
    render_bg(fruit.get_orange)


def play_with_magic_numbers():
    """Doc"""
    magic_numbers = {0, 1, 1, 2, 3, 5}

    for elem in magic_numbers:
        magic_numbers.add(get_next(elem))
    return magic_numbers


import sqlite3
import requests


class ResidentsDb:
    """Doc"""

    def __init__(self, table_name, mapping_function, duration):
        """Set location on disk data cache will reside.
        Also sets the table name and refresh duration
        """
        self.table_name = table_name
        self.mapping_function = mapping_function
        self.disk_location = DISK_LOCATION_DEFAULT
        self.duration = duration
        self.conn = None
        self.cursor = None

    def open(self):
        """Opens connection to sqlite database."""
        self.conn = sqlite3.connect(self.dbname)
        self.cursor = self.conn.cursor()

    def get_id_from_name(self, name):
        """Get id of resident from name."""
        data = self.cursor.execute("SELECT id FROM userdata WHERE Name ={};".format(name))
        self.conn.commit()
        return data


def fetch_version(request):
    """Fetch verison of bgmi."""
    version = requests.get("https://pypi.python.org/pypi/bgmi/json", verify=False).json()["info"]["version"]
    return version


no_ip_hosts = {"hostname": "gui-linux"}
empty_ip_hosts = {"hostname": "gui-linux", "ip_address": ""}
with_ip_hosts = {"hostname": "gui-linux", "ip_address": "111.111.111.111"}


def is_ip_address(hosts_dict):
    for key, value in hosts_dict.items():
        if key == "ip_address" and value is not None:
            return True

    return False


print(is_ip_address(no_ip_hosts))
print(is_ip_address(empty_ip_hosts))
print(is_ip_address(with_ip_hosts))

# O(len(N) + len(M))

from my_utils import get_file_names

files = get_file_names()
for file in files:
    if file.endswith(".py"):
        python_file_found = True
        break
else:
    python_file_found = False

    # bruh
