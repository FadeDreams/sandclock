import functools
import time
import inspect

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def sandclock(total_iters=1, precession=5, show_details=True):
    """measures the execution time of asynchronous/synchronous function in seconds.

    args:
        total_iters (int, optional): total number of iterations of the function. defaults to 1.
        precession (int, optional): precision of time in seconds. defaults to 5.
        show_details (bool, optional): whether each function execution time is printed. defaults to true.
    """
    def real_repeat(func):
        if inspect.iscoroutinefunction(func):
            ##
            @functools.wraps(func)
            async def wrapper_repeat(*args, **kwargs):
                print(f'{bcolors.OKBLUE}sandclock: Coroutine {func} with args {args} {kwargs}{bcolors.ENDC}')
                total_time = 0
                total_iter = 0
                for _ in range(total_iters):
                    current_iter = total_iter
                    if show_details:
                        print(f'{bcolors.OKCYAN}sandclock: Iter: {current_iter} started, {func} with args {args} {kwargs}{bcolors.ENDC}')
                    start = time.time()
                    await func(*args, **kwargs)
                    end = time.time()
                    total = end - start
                    total_time += total
                    total_iter += 1
                    if show_details:
                        print(f'{bcolors.OKCYAN}sandclock: Iter: {current_iter} finished, {func} in {total:.{precession}f} second(s){bcolors.ENDC}')
                print(f"{bcolors.OKGREEN}sandclock: total time: {total_time:.{precession}f} second(s), total iterations: {total_iter}{bcolors.ENDC}")
                return total_time
            return wrapper_repeat
            ##
        else:
            ##
            @functools.wraps(func)
            def wrapper_repeat(*args, **kwargs):
                print(f'{bcolors.OKBLUE}sandclock: None Coroutine {func} with args {args} {kwargs}{bcolors.ENDC}')
                total_time = 0
                total_iter = 0
                for _ in range(total_iters):
                    current_iter = total_iter
                    if show_details:
                        print(f'{bcolors.OKCYAN}sandclock: Iter: {current_iter} started, {func} with args {args} {kwargs}{bcolors.ENDC}')
                    start = time.time()
                    val = func(*args, **kwargs)
                    end = time.time()
                    total = end - start
                    total_time += total
                    total_iter += 1
                    if show_details:
                        print(f'{bcolors.OKCYAN}sandclock: Iter: {current_iter} finished, {func} in {total:.{precession}f} second(s){bcolors.ENDC}')
                    # print(f'val is {val}')
                    # return total_time
                print(f"{bcolors.OKGREEN}sandclock: total time: {total_time:.{precession}f}, total iterations: {total_iter}{bcolors.ENDC}")
                return total_time

            return wrapper_repeat

            ##
    return real_repeat

###

def sandclock_async(total_iters=1, precession=5, show_details=True) :
    """measures the execution time of asynchronous function in seconds.

    Args:
        total_iters (int, optional): total number of iterations of the function. Defaults to 1.
        precession (int, optional): precision of time in seconds . Defaults to 5.
        show_details (bool, optional): whether each function execution time is printed. Defaults to True.
    """
    def real_repeat(func):
        @functools.wraps(func)
        async def wrapper_repeat(*args, **kwargs):
            print(f'sandclock: Initialized {func} with args {args} {kwargs}')
            total_time = 0
            total_iter = 0
            for _ in range(total_iters):
                current_iter = total_iter
                if show_details:
                    print(f'sandclock: Iter: {current_iter} started, {func} with args {args} {kwargs}')
                start = time.time()
                await func(*args, **kwargs)
                end = time.time()
                total = end - start
                total_time += total
                total_iter += 1
                if show_details:
                    print(f'sandclock: Iter: {current_iter} finished, {func} in {total:.{precession}f} second(s)')
            print(f"sandclock: total time: {total_time:.{precession}f} second(s), total iterations: {total_iter}")
            return total_time

        return wrapper_repeat

    return real_repeat

def sandclock_sync(total_iters=2, precession=5, show_details=True) :
    """measures the execution time of synchronous function in seconds.

    Args:
        total_iters (int, optional): total number of iterations of the function. Defaults to 1.
        precession (int, optional): precision of time in seconds . Defaults to 5.
        show_details (bool, optional): whether each function execution time is printed. Defaults to True.
    """
    def repeat(func):
        if not inspect.iscoroutinefunction(func):
            print("not cor")

        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            print(f'sandclock: Initialized {func} with args {args} {kwargs}')
            total_time = 0
            total_iter = 0
            for _ in range(total_iters):
                current_iter = total_iter
                if show_details:
                    print(f'sandclock: Iter: {current_iter} started, {func} with args {args} {kwargs}')
                start = time.time()
                val = func(*args, **kwargs)
                end = time.time()
                total = end - start
                total_time += total
                total_iter += 1
                if show_details:
                    print(f'sandclock: Iter: {current_iter} finished, {func} in {total:.{precession}f} second(s)')
                # print(f'val is {val}')
                # return total_time
            print(f"sandclock: total time: {total_time:.{precession}f}, total iterations: {total_iter}")
            return total_time
        return wrapper_repeat

    return repeat

