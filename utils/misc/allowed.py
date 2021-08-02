def allow_access():
    def derorator(func):
        setattr(func, 'allow', True)
        return func
    return derorator