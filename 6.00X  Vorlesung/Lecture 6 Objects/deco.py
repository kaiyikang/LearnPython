def use_logging(func):
    def wrapper(*args,**kwargs):
        print("%s is runnning" %func.__name__)
        return func(*args,**kwargs)
    return wrapper

@use_logging
def bar():
    print('I am Bar')


bar()