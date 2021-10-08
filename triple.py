def tripler(f):
    ''' Creates a wrapper around a function that will repeat the function 3 times'''
    def wrap(*args, **kwargs):
        f(*args, **kwargs)
        f(*args, **kwargs)
        f(*args, **kwargs)
    return wrap
