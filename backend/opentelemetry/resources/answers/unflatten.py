def listify(obj: dict):
    keys = list(sorted((int(k) for k in obj.keys())))

    arr = [None] * (keys[-1] + 1)

    for key, value in obj.items():
        arr[int(key)] = value

    return arr


def propagate(obj: dict):
    for key, value in obj.items():
        if isinstance(value, dict) and value:
            if all(k.isdigit() for k in value.keys()):
                obj[key] = listify(propagate(value))
            else:
                obj[key] = propagate(value)
    return obj


def unflatten_json(d: dict):
    result = {}

    for key, value in d.items():
        key_elems = key.split(".")

        cur = result
        for elem in key_elems[:-1]:
            if elem not in cur:
                cur[elem] = {}
            cur = cur[elem]

        cur[key_elems[-1]] = value

    result = propagate(result)

    return result
