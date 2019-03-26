import time


# --exeTime
def exe_time(func):
    def new_func(*args, **args2):
        t0 = time.clock() * 1000
        print("@%s, {%s} start" % (time.strftime("%X", time.localtime()), func.__name__))
        back = func(*args, **args2)
        print("@%s, {%s} end" % (time.strftime("%X", time.localtime()), func.__name__))
        print("@%.3fs taken for {%s}" % (time.clock() * 1000 - t0, func.__name__))
        return back

    return new_func
# --end of exeTime
