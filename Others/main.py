import sys
from collections import deque, defaultdict
from typing import List, Optional


def step1(lines: List[Optional[int]]) -> Optional[int]:
    m = int(lines[1])
    stock_dict = dict()
    for i in range(2, m+2):
        d, s, p = map(int, lines[i].split())
        stock_dict[d] = s
    for i in range(m+2, len(lines)):
        line = lines[i].split()
        t = line[1]
        d = int(line[2])
        n = int(line[3])
        if stock_dict.get(d, 0) < n:
            print(f"sold out {t}")
        else:
            for _ in range(n):
                print(f"received order {t} {d}")
            stock_dict[d] -= n


"""
:param => d:料理番号｜s:初期在庫数｜p:価格
"""
def step2(lines: List[Optional[int]]) -> Optional[int]:
    m, k = map(int, lines[1].split())
    # stock_dict = dict()
    cooking = defaultdict(int)
    wait_q = deque()
    # # メニュー情報の記録
    # for i in range(2, m+2):
    #     d, s, p = map(int, lines[i].split())
    #     stock_dict[d] = s
    for i in range(m+2, len(lines)):
        line = lines[i].split() # received order 10 100 => ["received", "order", "10", "100"]｜complete 101 => ["complete", "101"]
        if line[0] == "received":
            t = int(line[2])
            d = int(line[3])
            # すぐに作り始められるかを判断
            if k >= 1:
                print(d)
                cooking[d] += 1
                k -= 1
            else:
                print("wait")
                wait_q.append(d)

        elif line[0] == "complete":
            d = int(line[1])
            if cooking.get(d, 0) >= 1:
                cooking[d] -= 1
                if cooking[d] == 0:
                    del cooking[d]
                k += 1

                if wait_q:
                    next_d = wait_q.popleft()
                    cooking[next_d] += 1
                    k -= 1
                    print(f"ok {next_d}")
                else:
                    print("ok")
            else:
                print("unexpected input")


def step3(lines: List[Optional[int]]) -> Optional[tuple[int, int]]:
    m = int(lines[1])
    cooking_q = deque()
    not_match_q = deque()

    for i in range(m+2, len(lines)):
        line = lines[i].split()
        if line[0] == "received":
            t = int(line[2])
            d = int(line[3])
            cooking_q.append((t, d))
        elif line[0] == "complete":
            d = int(line[1])
            if cooking_q:
                for _ in range(len(cooking_q)):
                    d_tuple = cooking_q.popleft()
                    if d_tuple[1] == d:
                        print(f"ready {d_tuple[0]} {d_tuple[1]}")
                        if not_match_q:
                            cooking_q = not_match_q + cooking_q
                    else:
                        not_match_q.append(d_tuple)


def main(lines):
    step = lines[0]
    if step == '1':
        step1(lines)
    if step == '2':
        step2(lines)
    if step == '3':
        step3(lines)



if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))  # 改行を取り除いて追加
    main(lines)
