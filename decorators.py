
def decorator(func):

    def decorated():

        print('함수 시작!')

        func()

        print('함수 끝!+_+')

    return decorated



@decorator

def hello_world():



    print('Hello_World^^')




hello_world()
