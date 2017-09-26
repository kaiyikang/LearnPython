def log(func):
    def wrapper(*args,**kwargs):
        print("this is function : %s" % func.__name__)
        return func(*args,**kwargs)
    return wrapper

@log
def bar():
    print('I have a bar')

bar()