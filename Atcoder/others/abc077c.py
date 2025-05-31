import bisect
import random

coupons = ['A', 'B', 'C', 'D']
weights = [10, 30, 20, 40]

# 累積和（[10, 40, 60, 100]）
cum_weights = [sum(weights[:i+1]) for i in range(len(weights))]

# bisect_right を使って rand_num が入る位置を探す
def select_coupon(rand_num):
    return coupons[bisect.bisect_right(cum_weights, rand_num)]

def main():
    n = random.randint(1, 100)
    print(n)
    print(select_coupon(n))

if __name__ == '__main__':
    main()