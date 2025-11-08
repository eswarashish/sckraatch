from functools import wraps

def enforce_strict(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print("Enforcing strict type check")
        hints = func.__annotations__
        # the above line is to get the type hints
        all_args = list(args)+list(kwargs.values())

        for name, expected_type in hints.items():
            if name != 'return':
                try:
                    arg_value =all_args[list(hints.keys()).index(name)]
                    if not isinstance(arg_value,expected_type):
                        raise TypeError(
                            f"arg '{name}' passed, expected type '{expected_type.__name__}' "
                            f"but recieved '{type(arg_value).__name__}'"
                        )
                except IndexError:
                    raise IndexError(
                        f"Required '{name}' of type '{expected_type.__name__}'"
                    )
                
        return func(*args,**kwargs)
    
    return wrapper

@enforce_strict
def add(x:int, y:int):
    return x+y

print(add(5,10)  )      