T = int(input())
for _ in range(T):
    N = int(input())
    S = input()
    # point-1: 状態0を考えることで0-indexを楽にする
    S = '0' + S
    """
    tips-1: 
    - 1 << N は1を左にN回シフトしたものである => N=2の場合... 100(4)
    - すなわち 1<<N は 2^N と同義
    - また、1<<N は10進数表記なので 1<<2 == 4
    """
    # point-2: 状態を表す配列の用意
    ok = [0 for _ in range(1 << N)]
    # point-3: 状態0のフラグを立てる
    ok[0] = 1

    # point-4: bit全探索 => すべての状態を探索する
    for i in range(1 << N):
        # point-5: 状態iに達したかどうかを判断する => 達した状態から次の状態への遷移を考える
        if ok[i] == 0:
            continue
        # point-6: jは液体の種類のindex
        for j in range(N):
            # point-7: 状態iの中でj番目の薬品のビットが立っているか（その薬品もう使ったのか判定）
            if i & (1 << j):
                continue
            # point-8: 状態iに薬品jを新たに追加する => 1 << j のビットフラグを立てる　next は瓶の中身を表す
            next = i | (1 << j)
            # point-9: 状態 next が大丈夫な組み合わせか判断 => 状態nextは確認済みとする
            if S[next] == '0':
                ok[next] += 1

    if ok[(1<<N)-1]:
        print("Yes")
    else:
        print("No")




