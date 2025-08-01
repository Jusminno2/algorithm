"""
- クエリを処理していくと配列Aの長さは最大で10^14となる
　-> Aをそのまま配列として保持することは困難

- ここで追加クエリごとの（c, x）の組を列として保持する
　<=> Aを連長圧縮（ランレングス圧縮）した列で考える

- Aに対して削除クエリを行う方法を考える
　1. A の先頭から順に (c,x) の組を見ていく
　2. if c ≤ k：整数の削除し再び先頭から削除する操作を続け
     if c > k：先頭の整数の組を (c−k,x) に置き換え削除をやめる

- 追加クエリでは整数の組は 1 個追加され、一連削除クエリでは高々追加された整数の組の数しか削除せず、各クエリでは高々
　 1 つの整数の組に対して変更の操作を行う。そのため、時間計算量 O(Q) で解くことができる。
"""

from collections import deque


def main() -> None:
    q = int(input())

    # 各追加クエリを (残り個数 c, 値 x) のペアで保持
    """
    データ構造選択理由；
    「末尾へ追加／先頭から削除」を繰り返す典型的 FIFO ワークロードなので、先頭操作が O(1) の deque が最適
    
    なぜ、whileループなのか？
    -> 取得クエリでは「先頭の (c, x) を 必要個数 k が尽きるまで 繰り返し 消費する」という手順が本質的
    -> つまり「条件 k > 0 and キュー非空 が満たされる間、同じ処理を連続実行」＝ while が自然
    
    ほかとの比較
    -> forループの場合、queを途中でpopleft()するとイテレータが壊れる
    　　-> 削りながら列挙は、forループに向かない
    
    計算量 - O(Q)
    1. 追加クエリの場合 - O(1)
       -> 1 c x：値 x を c 個、末尾に追加
    2. クエリ削除 - O(1)
       -> deque の先頭から k 個分だけ (c, x) を処理して加算＆削除（最大で O(1) 回の操作 × 個数）
       -> 1つの削除クエリが多くのペアを処理することがあっても、そのペアは再び処理されることはない
            -> 一回でQ個に近いペアを削除したとしても、その後は少ない数の削除になる、だからならしたら、毎回
            　　のクエリでは、平均O(1)となる。この「毎回のクエリごと」の考え方が大事！
    """
    que: deque[list[int]] = deque()

    for _ in range(q):
        nums = list(map(int, input().split()))
        q_type = nums[0]

        if q_type == 1:
            # 追加クエリ: c 個の値 x を末尾に追加
            _, c, x = nums
            que.append([c, x])
        else:
            # 取得クエリ: 先頭から k 個取り出して総和を出力
            _, k = nums
            ans = 0

            # 先頭グループを順に消費
            while que and que[0][0] <= k:
                c, x = que.popleft()
                ans += c * x
                k -= c

            # まだ k 個残っている場合は，先頭グループを分割
            if k:
                que[0][0] -= k  # 残数を更新
                ans += k * que[0][1]  # 部分的に消費した分を加算

            print(ans)
        print(list(que))


if __name__ == "__main__":
    main()
