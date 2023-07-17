no_ip_hosts = {"hostname": "gui-linux"}
empty_ip_hosts = {"hostname": "gui-linux", "ip_address": ""}
with_ip_hosts = {"hostname": "gui-linux", "ip_address": "111.111.111.111"}


def is_ip_address(hosts_dict):
    return any(key == "ip_address" and value is not None for key, value in hosts_dict.items())


print(is_ip_address(no_ip_hosts))
print(is_ip_address(empty_ip_hosts))
print(is_ip_address(with_ip_hosts))

# O(len(N) + len(M))
