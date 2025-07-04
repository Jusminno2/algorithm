class UnionFind:
    """
    本スクリプトは経路圧縮だけを採用している
    """
    def __init__(self, n):
        # parents は各要素の親を表す配列
        self.parents = list(range(n))

    def find(self, x):
        # 自分自身が親であるかを判定
        if self.parents[x] == x:
            return x
        # xの親が自分自身ではない場合、xの親の親を探してx自身の親として再登録する（経路圧縮）
        else:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        # 親を探してくる
        root_x, root_y = self.find(x), self.find(y)
        # 親が同じ場合 => 何もしない
        if root_x == root_y: return
        # 親が異なる場合 => root_xの親をroot_yとする
        self.parents[root_x] = root_y

    def same(self, x, y):
        return self.find(x) == self.find(y)

n, q = map(int, input().split())
uf = UnionFind(n)

for _ in range(q):
    p, a, b = map(int, input().split())
    if p:
        print('Yes' if uf.same(a, b) else 'No')
    else:
        uf.union(a, b)

