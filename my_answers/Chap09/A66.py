# Union-Find 木
class unionfind(object):
    # n 頂点の Union-Find 木を作成
    def __init__(self, n):
        self.n = n
        self.parent = [-1 for _ in range(n+1)]
        self.size = [1 for _ in range(n+1)]

    # 頂点 x の根を返すメソッド
    def root(self, x: int) -> int:
        while self.parent[x] != -1:
            x = self.parent[x]
        return x

    # 要素 u,v を統合する関数
    def unite(self, u: int, v: int) -> None:
        root_u = self.root(u)
        root_v = self.root(v)
        if root_u != root_v:
            if self.size[root_u] < self.size[root_v]:
                self.parent[root_u] = root_v
                self.size[root_v] += self.size[root_u]
            else:
                self.parent[root_v] = root_u
                self.size[root_u] += self.size[root_v]

    # 要素 u と v が同一のグループかどうかを返す関数
    def same(self, u: int, v: int) -> bool:
        return self.root(u) == self.root(v)


# 入力
N, Q = map(int, input().split())
queries = [list(map(int, input().split())) for _ in range(Q)]

# クエリの処理
uf = unionfind(N)
for tp, u, v in queries:
    if tp == 1:
        uf.unite(u, v)
    if tp == 2:
        if uf.same(u, v):
            print("YES")
        else:
            print("NO")
