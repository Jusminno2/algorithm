import sys
import bisect
from typing import List


def find_first_unreserved(reserved: List[int], l: int, r: int) -> int:

    # l以上の最初の予約済み枠のインデックスを二分探索で取得
    start_idx = bisect.bisect_left(reserved, l)

    current = l  # 現在チェック中の枠番号

    # 関連する予約済み枠を順番にチェック
    for j in range(start_idx, len(reserved)):
        # r を超えた予約枠に到達したら処理終了
        if reserved[j] > r:
            break

        # 隙間が見つかった場合
        if current < reserved[j]:
            # 隙間内の最初の枠が範囲内かチェック
            if current <= r:
                return current

        # 予約済み枠の次に移動
        current = reserved[j] + 1

    # 最後の予約枠以降をチェック
    if current <= r:
        return current
    else:
        return -1  # 全て予約済み


def main(lines: List[int]) -> List[str]:

    # 入力条件
    n, m = map(int, lines[0].split())

    # 予約済み枠リスト（空の場合も対応）
    if m == 0:
        reserved = []
    else:
        reserved = list(map(int, lines[1].split()))

    # クエリ数取得
    q = int(lines[2])

    results = []

    # 各クエリを処理
    for i in range(q):
        l, r = map(int, lines[3 + i].split())

        # [l, r] 範囲内で最初の未予約枠を見つける
        answer = find_first_unreserved(reserved, l, r)
        results.append(str(answer))

    return results


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))

    results = main(lines)
    for result in results:
        print(result)