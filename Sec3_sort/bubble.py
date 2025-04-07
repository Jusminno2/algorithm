from typing import List


"""
【型ヒント（Type Hint）という記述法】
・arr: List[int]：引数 arr は「整数のリスト（List[int]）」であると示す
・これを使うために、最初の行で from typing import List と書いている
・-> List[int]：この関数は「整数のリスト」を返すという意味
【メリット】
・コードの可読性が向上する。
・IDE（統合開発環境）での補完や警告が便利になる。
・他人が関数の使い方を理解しやすくなる。
"""
def bubble_sort(arr: List[int]) -> List[int]:
    length = len(arr)
    for i in range(length):
        for j in range(length - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

"""
【if __name__ == '__main__'】
・スクリプトが直接実行されたときにだけ、特定の処理を行うためのおまじない
・'__main__'：このスクリプトが「直接実行された場合」のみに __name__ がこの値になる
・他のファイルから import して使った場合には実行されない
・テストやデモコードをここに書くことができる
"""
if __name__ == '__main__' :
    # arr = [2,5,1,8,7,4]
    import random
    arr = [random.randint(0, 10000) for i in range(10)]
    bubble_sort(arr)
    print(arr)