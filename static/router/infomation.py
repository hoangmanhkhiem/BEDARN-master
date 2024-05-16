import json


def get_config_by_room(path_room):
    config_list = []
    try:
        with open(path_room, 'r') as f:
            room = json.load(f)
            for key in room:
                k = key['id'], key['name'], key['status'], key['os'], key['cpu'], key['memory'], key['disk'], key[
                    'network']
                config_list.append(k)
    except:
        return None
    return config_list, len(config_list)


def get_full_config():
    path_const = "../../static/data/"
    list_config = []
    try:
        # Duyet het tat ca cac file trong folder data
        for i in range(3, 5):
            name = "40" + str(i)
            path_room = path_const + name + ".json"
            list_config.extend(get_config_by_room(path_room))
    except:
        return None
    return list_config, len(list_config)


def get_id_name_status(path_room):
    config_list = []
    try:
        with open(path_room, 'r') as f:
            room = json.load(f)
            for key in room:
                k = key['id'], key['name'], key['status']
                config_list.append(k)
    except:
        return None
    return config_list, len(config_list)


def get_full_id_name_status():
    path_const = "../../static/data/"
    list_config = []
    try:
        # Duyet het tat ca cac file trong folder data
        for i in range(3, 5):
            name = "40" + str(i)
            path_room = path_const + name + ".json"
            list_config.extend(get_id_name_status(path_room))
    except:
        return None
    return list_config, len(list_config)


def get_pathvm_by_room(room):
    path_const = "../../static/data/"
    path_list = []
    try:
        name = "40" + str(room)
        path_room = path_const + name + ".json"
        with open(path_room, 'r') as f:
            room = json.load(f)
            for key in room:
                path_list.append(key['path'])
    except:
        return None
    return None


def get_all_vmpath():
    path_const = "../../static/data/"
    path_list = []
    try:
        for i in range(3, 5):
            name = "40" + str(i)
            path_room = path_const + name + ".json"
            with open(path_room, 'r') as f:
                room = json.load(f)
                for key in room:
                    k = key['path'], key['id']
                    path_list.append(k)
    except:
        return None
    return path_list
