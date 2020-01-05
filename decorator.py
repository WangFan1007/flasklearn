

def params_de(params):
    print(params)

    def indeco(func):
        print("indeco")
        return func
    return indeco


def route(func):
    print("in route")
    return func


@route
def test():
    print("Hello test")


@params_de("hello prams")
def test2():
    print("test2")


# if __name__ == '__main__':
#     # test()
#     print("123")
