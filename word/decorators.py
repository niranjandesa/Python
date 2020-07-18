from time import time
def decorator1(f):
    def subdec(*args,**kwargs):
        resp=f(*args,**kwargs)
        if type(resp)==set:
            no=1
            for i in resp:
                print("{}){}".format(no,i))
                no=no+1
    return subdec


def performance(fn):
    def wrapper(*args,**kwargs):
        t1=time()
        result=fn(*args,**kwargs)
        t2=time()
        print(f'{fn.__name__} time took : {t2-t1} sec')
        return result
    return wrapper
