from functools import wraps
from decorators import enforce_strict

def logger(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        all_args = list(args)+list(kwargs.values())
        with open('logfile.txt',mode='a') as f:
            f.write(f'{func.__name__} called with args {all_args}\n')
            f.close()
        x = func(*args,**kwargs)
        print("logger executed")
        return x
    return wrapper

@enforce_strict
@logger
def subtract(x:int,y:int):
    return x-y

print(subtract(3,4))