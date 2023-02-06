def make_caller(func, *args, **kwargs):
    def caller():
        return func(*args, **kwargs)
    return caller
