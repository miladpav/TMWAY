from os import path, mkdir
import re


## --------------------------------------------------------------------- ##

# create group for server_name
def groupCreator(pattern_list, hostname):

    for hostname_pattern in pattern_list:
        if not re.match(hostname_pattern, hostname):
            group_of_hostname = 'uncategorized'
        search_in_hostname = re.search(hostname_pattern, hostname)
        if search_in_hostname:
            group_of_hostname = search_in_hostname.group(1)
            break
    return group_of_hostname


# make buffer of file
def make_buffer(file):
    if path.exists(file):
        with open(file, 'r') as inventory:
            content = inventory.readlines()
        return content
    else:
        content = []
        return content


def check_directory(file):
    directory_path = path.dirname(file)
    if not path.exists(directory_path):
        mkdir(directory_path)


# insert data of inventory
def insert_line(content, ip_address, hostname, group_of_hostname, invfile, owner_group):
    if owner_group in 'all':
        newHost = f"{hostname} ansible_host={ip_address}\n"
    else:
        newHost = f"{hostname} ansible_host={ip_address} owner_group={owner_group}\n"
    groupOfHost = f"[{group_of_hostname}]\n"
    if newHost not in content:
        if groupOfHost not in content:
            with open(invfile, 'a+') as inventory_file:
                # FIXME: this section is not clean, need to improve endlines of file
                if len(content) != 0:
                    if str(content[-1]) != "\n":
                        inventory_file.write("\n")
                inventory_file.write(groupOfHost)
                inventory_file.write(newHost)
        else:
            Index_of_Group = content.index(groupOfHost)
            content.insert(Index_of_Group + 1, newHost)
            with open(invfile, 'w+') as inventory_file:
                content = "".join(content)
                inventory_file.write(content)
    return {"status": "ok", "message": "your ip address added to inventory successfully"}
