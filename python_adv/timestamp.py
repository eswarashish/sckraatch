from functools import wraps
from decorators import enforce_strict
from logger import logger
import dateutil

def timestamp(func):
    @wraps(func) # this decorator is added to make sure function metadata would be of func not wrapper because when used the properties like __name__, __annotations__ so not to miss metadata of main functions
    def wrapper(*args,**kwargs):
        with open('timestamp.txt',mode='a') as f:
            f.write(f"Function {func.__name__} called at {dateutil.utils.today()}")
            f.close()
        x = func(*args,**kwargs)
        print(f"Timestamp added")
        return x
    return wrapper

@logger
@enforce_strict
@timestamp
def mul(x:int,y:int):
    return x*y

print(mul(3,4))