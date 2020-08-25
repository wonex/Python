from time import time 

def timer(fun):
    def f(*args, **kwargs):
        begin = time()
        out = fun(*args, **kwargs)
        print(time() - begin)
        return out
    return f

@timer
def add(x, y, z=10):
    return x + y + z

if __name__ == '__main__':
    print(add(2, 3, 4))
