import time # cacheを使うことで実行速度がはやくなる例


def memorize(f):
    cache = {}
    def _wrapper(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return _wrapper

"""
デコレーターはどんなとき使う？
=> ある関数の処理の前後で別処理を実行したいとき（例：cache, 挨拶）
"""
@memorize
def long_func(num: int) -> int:
    r = 0
    for i in range(10000000):
        r += num * i
    return r


if __name__ == '__main__':
    for i in range(10):
        print(long_func(i))

    start_time = time.time()
    for i in range(10):
        print(long_func(i))
    print(time.time() - start_time)