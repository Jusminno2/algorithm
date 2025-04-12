import hashlib
from typing import Any



class HashTable(object):

    def __init__(self, size=10) -> None:
        self.size = size
        self.table = [[] for _ in range(self.size)]

    # [key, value] を格納するindexを決定する=>返り値：index
    def hash(self, key) -> int:
        return int(hashlib.md5(key.encode()).hexdigest(), base=16) % self.size

    # key に重複があった場合は、valueを上書きする
    def add(self, key, value) -> None:
        index = self.hash(key)
        # indexが同じ場合...keyまで一致しているのかを調べる
        """
        for-else構文：for文がbreakで終了した場合、elseはスキップ
        　　　　　　　　breakにかからなかった場合、else内の処理が実行される
        """
        for data in self.table[index]:
            if data[0] == key:
                data[1] = value
                break
        else:
            self.table[index].append([key, value])

    def print(self) -> None:
        for index in range(self.size):
            print(index, end=' ')
            for data in self.table[index]:
                print('-->', end=' ')
                print(data, end=' ')
            print() # 改行のため

    def get(self, key) -> Any:
        index = self.hash(key)
        for data in self.table[index]:
            if data[0] == key:
                return data[1]

    # python での辞書型の追加の記述方法を用いた際にこちらの関数が呼び出される
    def __setitem__(self, key, value) -> None:
        self.add(key, value)

    def __getitem__(self, key) -> Any:
        return self.get(key)


if __name__ == "__main__":
    hash_table = HashTable()
    # 記述方法が実際のpythonコードとことなる
    # hash_table.add('car', 'Tesla')
    # hash_table.add('car', 'Tesla')
    # hash_table.add('pc', 'Mac')
    # hash_table.add('sns', 'YouTube')
    hash_table['car'] = 'Tesla'
    hash_table['car'] = 'Tesla'
    hash_table['pc'] = 'Mac'
    hash_table['sns'] = 'YouTube'
    print(hash_table.get('sns'))
    print()
    hash_table.print()
    # 以下のようにpythonでは記述する
