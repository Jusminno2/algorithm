"""
point:
- 回文の判定
- N進法をどうやって導くか？
"""
def check_palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False

def base_n(num_10,n):
    str_n = ''
    while num_10:
        if num_10 % n >= 10:
            return -1
        str_n += str(num_10%n)
        num_10 //= n
    return int(str_n[::-1])


def main():
    A = int(input())
    N = int(input())
    ans = 0

    for i in range(N):
        if check_palindrome(str(i)) and check_palindrome(str(base_n(i, A))):
            ans += i

    print(ans)




if __name__ == '__main__':
    main()