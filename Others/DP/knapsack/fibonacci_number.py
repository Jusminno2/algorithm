def fibonacci(n: int) -> int:
    memo = [-1 for _ in range(n + 1)]
    memo[0] = 1
    memo[1] = 1

    def _fibonacci(n: int) -> int:
        if memo[n] != -1:
            return memo[n]
        memo[n] = _fibonacci(n - 1) + _fibonacci(n - 2)
        return memo[n]

    return _fibonacci(n)


if __name__ == '__main__':
    n = int(input())
    print(fibonacci(n))
