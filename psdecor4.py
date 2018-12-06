def to_json(func):
    """wrap return values"""

    def json_handler(*args):
        from json import dumps

        return dumps(func(*args))

    return json_handler


@to_json
def compute(a, b):
    return a + b, a * b


print(compute(33, 22))
