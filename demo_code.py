import json

json.loads(f.read())

def f():
    """
    x
    y

    z
    """

    f.write(json.dumps('"abc"'))
