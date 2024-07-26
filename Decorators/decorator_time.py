from functools import wraps

def time_it(func):
    import time
    @wraps(func)
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f'time taken by {func.__name__}is {time.time()-start}')
        return result
    return  wrapper
    

@time_it
def fib(num):
    current,prev = 1,0
    for i in range(num):
        current,prev = current+prev,current
    return (current)

print(fib(10))