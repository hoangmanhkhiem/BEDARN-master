import json
import json


def get_list_ip(path_room):
    ip_list = []
    try:
        with open(path_room, 'r') as f:
            room = json.load(f)
            for key in room:
                ip_list.append(key['ip'])
    except:
        return None
    return ip_list


def get_list_full_ip():
    path_const = "../static/data/"
    list_ip = []
    try:
        # Duyet het tat ca cac file trong folder data
        for i in range(1, 9):
            name = "40" + str(i)
            path_room = path_const + name + ".json"
            list_ip.extend(get_list_ip(path_room))
    except:
        return None
    return list_ip


def set_ip_by_id(id, ip, name):
    config_list = []
    try:
        with open(name, 'r') as f:
            room = json.load(f)
            for key in room:
                if key['id'] == id:
                    key['ip'] = ip
                config_list.append(key)
        with open(name, 'w') as f:
            json.dump(config_list, f)

    except:
        return 0
    return 1


def get_ip_by_id(id, name):
    try:
        with open(name, 'r') as f:
            room = json.load(f)
            for key in room:
                if key['id'] == id:
                    return key['ip']
    except:
        return None
    return None


def scan_id_in_range(start, end):
    path_const = "../static/data/"
    config_list = []
    try:
        # Duyet het tat ca cac file trong folder data
        for i in range(start, end):
            name = "40" + str(i)
            path_room = path_const + name + ".json"
            with open(path_room, 'r') as f:
                room = json.load(f)
                for key in room:
                    if end > key['id'] > start:
                        k = key['id'], key['name'], key['status'], key['ip'], key['network']
                        config_list.append(k)
    except:
        return None
    return config_list
