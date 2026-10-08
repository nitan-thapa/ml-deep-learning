


def authorization(fun):
    def inner(role):
        if(role=="seller"):
            fun()
        else :
            print("you are not seller")
    

    return inner


@authorization
def addProduct():
    print("add product in the list")


addProduct("buyer")

