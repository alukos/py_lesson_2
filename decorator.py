def my_decorator(func):
    def wrapper(*args,**kwargs):
        print('Pre logic',args)
        func(*args,**kwargs)
        print('post logic')
    return wrapper


@my_decorator
def test(name:str):
    print(f"in test {name}")

test('Alex')
print('_________________________________________')

def my_decorator2(path:str,method:str):
    def my_decorator(func):
        def wrapper(*args,**kwargs):
            print(path,method)
            func(*args,**kwargs)
        return wrapper
    return my_decorator

@my_decorator2(11,'Ivanov')
def test2(name:str):
    print(f"in test2 {name}")

test2('Alex')
print('_________________________________________')

@my_decorator
@my_decorator2('/','GET')
def test3():
    print('Im test 3')

test3()