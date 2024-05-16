import json


def getuser_by_id_room(id):
    path = "../../static/user_data/user_list.json"
    try:
        with open(path, 'r') as f:
            user = json.load(f)
            for key in user:
                if key['id'] == id:
                    return key['username'], key['password']
    except:
        return None
    return None