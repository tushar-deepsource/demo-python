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
