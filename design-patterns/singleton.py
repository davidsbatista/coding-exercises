def singleton(cls):
    instances = {}

    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]

    return getinstance


@singleton
def Duck():
    pass

duck_one = Duck()
duck_two = Duck()

print duck_one == duck_two
