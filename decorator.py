def notify_observed(message=""):
    def decorated_method(func):
        def wrapper(obj, *args, **kwargs):
            result = func(obj, *args, **kwargs)
            for observe in obj.observers:
                observe.send(message)
            return result
        return wrapper
    return decorated_method
