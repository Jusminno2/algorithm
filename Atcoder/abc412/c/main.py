import bisect

T = int(input())

"""
 戦法：
 ・ナップサック問題と考えたときに、行=dominoということまではわかるが、カラムをどうするかわからん
 ・と思ったけど、制約条件的にn回for文回したらO(T*N)でアウト
 ・ソートアルゴリズムはO(NlogN)のため使えないと思ったが、すべてのテストケースの総和的におっけ
 ・最小個数だけ出せば良いから、割り算した数だけ出せば良い => while??
 
 ・1番目とn番目の割り算は必要そう
 
 メモ：
 ・仮に [1 3 2 5] の場合...
 　  ・1 5 は確定している => 5 // 1 = 5 より一発では無理 => 5 / 2 = 2.5（base） > 2 * S1より
      => 2 * S1 以下のものを探す（second とする） 
      => second*2 が base より大きければ base <= n <= second*2 となる n を探す
      => 以下繰り返す
      
 ・[298077099 766294630 440423914 59187620 725560241 585990757 965580536 623321126 550925214 917827435]
    ・298077099 917827435 は確定
"""

for _ in range(T):
    domino_num = int(input())
    domino_list = list(map(int, input().split()))

    first = domino_list[0]
    last = domino_list[-1]

    sorted_domino_list = sorted(domino_list)

    count = 2
    current = first
    next_id = 1

    while current * 2 <= last:
        current_id = next_id - 1
        next_id = bisect.bisect_right(sorted_domino_list, current * 2)
        if (next_id-1) == current_id:
            print(-1)
            exit()
        else:
            current = sorted_domino_list[next_id-1]
            count += 1

    print(count)










