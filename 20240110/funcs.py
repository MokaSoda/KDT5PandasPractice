def add(x, y):
    return x+y
div = lambda x, y : x / y if y != 0 else None


if __name__ == '__main__':
    print(f"add(3,4) : {add(3, 4)}")
    print(f"div(3,4) : {div(3, 4)}")
    print(f"funcs.py => __name__ : {__name__}")
