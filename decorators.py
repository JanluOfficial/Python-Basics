def mydecorator(function):
    def wrapper(data):
        ### stuff before 
        result = function(f"Hello {data}")
        ### stuff after
        return result
    return wrapper

@mydecorator
def myfunction(name):
    print(name)
myfunction('Joshua')
