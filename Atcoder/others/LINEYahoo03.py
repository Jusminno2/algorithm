import sys
import math

# ストレージ設定
STORAGE_PRICES = {"storage_A1": 0.01, "storage_A2": 0.001, "storage_B1": 0.01, "storage_B2": 0.0001}
UPDATE_PRICES = {"storage_A1": 0.0005, "storage_A2": 0.01, "storage_B1": 0.001, "storage_B2": 0.5}
FREE_PLAN_AVAILABLE = {"storage_A1": True, "storage_A2": True, "storage_B1": False, "storage_B2": False}
FREE_PLAN_BASE_FEE = 1000


def calculate_storage_usage_mb(files, storage_name):
    """指定ストレージの現在の利用量をMB単位で計算（小数点以下切り上げ）"""
    if len(files[storage_name]) == 0:
        return 0
    total_kb = sum(files[storage_name].values())
    return math.ceil(total_kb / 1000)


def calculate_total_fees(files, monthly_updates, max_storage_usage_mb):
    """月次の総料金を計算する（最大利用量を使用）"""
    total_storage_fee = 0
    total_update_fee = 0

    for storage_name in files:
        # 保存料金の計算（月中の最大利用量を使用）
        max_usage_mb = max_storage_usage_mb[storage_name]
        if max_usage_mb > 0:
            storage_fee = math.ceil(max_usage_mb * STORAGE_PRICES[storage_name])
            total_storage_fee += storage_fee

        # 更新料金の計算
        if monthly_updates[storage_name] > 0:
            update_mb = math.ceil(monthly_updates[storage_name] / 1000)
            update_fee = math.ceil(update_mb * UPDATE_PRICES[storage_name])
            total_update_fee += update_fee

    # 利用料金の計算
    usage_fee = max(0, total_storage_fee + total_update_fee - FREE_PLAN_BASE_FEE)

    return total_storage_fee, total_update_fee, usage_fee


def check_free_plan_storage_constraint(storage_name):
    """無料プランでのストレージ利用可能かをチェック"""
    if not FREE_PLAN_AVAILABLE[storage_name]:
        return "this storage location is not available on the free plan"
    return None


def check_free_plan_fee_constraint(files, monthly_updates, max_storage_usage_mb):
    """無料プランでの料金制限をチェック"""
    _, _, usage_fee = calculate_total_fees(files, monthly_updates, max_storage_usage_mb)
    return usage_fee > 0


def update_max_storage_usage(files, storage_name, max_storage_usage_mb):
    """指定ストレージの最大利用量を更新"""
    current_usage_mb = calculate_storage_usage_mb(files, storage_name)
    max_storage_usage_mb[storage_name] = max(max_storage_usage_mb[storage_name], current_usage_mb)


def process_upload(storage_name, filename, filesize_kb, files, monthly_updates, max_storage_usage_mb):
    """アップロード処理"""
    # 無料プランのストレージ制約チェック
    constraint_error = check_free_plan_storage_constraint(storage_name)
    if constraint_error:
        return f"UPLOAD: {constraint_error}"

    # ファイル重複チェック
    if filename in files[storage_name]:
        return "UPLOAD: file already exists"

    # 仮にファイルを追加し、更新量も追加
    files[storage_name][filename] = filesize_kb
    monthly_updates[storage_name] += filesize_kb

    # 最大利用量を更新
    update_max_storage_usage(files, storage_name, max_storage_usage_mb)

    # 料金制限チェック
    if check_free_plan_fee_constraint(files, monthly_updates, max_storage_usage_mb):
        # 追加を取り消し
        del files[storage_name][filename]
        monthly_updates[storage_name] -= filesize_kb
        # 最大利用量を再計算（取り消し後）
        update_max_storage_usage(files, storage_name, max_storage_usage_mb)
        return "UPLOAD: free plan fee limit exceeded"

    # 成功時の料金出力
    storage_fee, update_fee, usage_fee = calculate_total_fees(files, monthly_updates, max_storage_usage_mb)
    return f"UPLOAD: {storage_fee} {update_fee} {usage_fee}"


def process_delete(storage_name, filename, files, monthly_updates, max_storage_usage_mb):
    """削除処理"""
    # 無料プランのストレージ制約チェック
    constraint_error = check_free_plan_storage_constraint(storage_name)
    if constraint_error:
        return f"DELETE: {constraint_error}"

    # ファイル存在チェック
    if filename not in files[storage_name]:
        return "DELETE: file does not exist"

    # 削除対象ファイルのサイズを取得
    deleted_filesize = files[storage_name][filename]

    # 更新量を追加（削除による更新量）
    monthly_updates[storage_name] += deleted_filesize

    # 現在の更新料金を計算
    _, current_update_fee, _ = calculate_total_fees(files, monthly_updates, max_storage_usage_mb)

    # DELETE処理では月中の最大保存料金を使用
    total_max_storage_fee = 0
    for storage in max_storage_usage_mb:
        max_usage_mb = max_storage_usage_mb[storage]
        if max_usage_mb > 0:
            storage_fee = math.ceil(max_usage_mb * STORAGE_PRICES[storage])
            total_max_storage_fee += storage_fee

    # 利用料金を計算（最大保存料金 + 現在の更新料金）
    usage_fee = max(0, total_max_storage_fee + current_update_fee - FREE_PLAN_BASE_FEE)

    # 料金出力用の結果を保存
    output_result = f"DELETE: {total_max_storage_fee} {current_update_fee} {usage_fee}"

    # 実際にファイルを削除
    del files[storage_name][filename]

    # 料金制限チェック（削除後の状態で）
    if check_free_plan_fee_constraint(files, monthly_updates, max_storage_usage_mb):
        # 削除を取り消し
        files[storage_name][filename] = deleted_filesize
        monthly_updates[storage_name] -= deleted_filesize
        return "DELETE: free plan fee limit exceeded"

    # 成功時は月中の最大保存料金 + 現在の更新料金を出力
    return output_result


def process_update(storage_name, filename, new_filesize_kb, files, monthly_updates, max_storage_usage_mb):
    """更新処理"""
    # 無料プランのストレージ制約チェック
    constraint_error = check_free_plan_storage_constraint(storage_name)
    if constraint_error:
        return f"UPDATE: {constraint_error}"

    # ファイル存在チェック
    if filename not in files[storage_name]:
        return "UPDATE: file does not exist"

    # 仮にファイルを更新し、新しいファイルサイズ全体を更新量に追加
    old_filesize = files[storage_name][filename]
    files[storage_name][filename] = new_filesize_kb
    monthly_updates[storage_name] += new_filesize_kb  # 新しいファイルサイズ全体

    # 最大利用量を更新
    update_max_storage_usage(files, storage_name, max_storage_usage_mb)

    # 料金制限チェック
    if check_free_plan_fee_constraint(files, monthly_updates, max_storage_usage_mb):
        # 更新を取り消し
        files[storage_name][filename] = old_filesize
        monthly_updates[storage_name] -= new_filesize_kb
        # 最大利用量を再計算（取り消し後）
        update_max_storage_usage(files, storage_name, max_storage_usage_mb)
        return "UPDATE: free plan fee limit exceeded"

    # 成功時の料金出力
    storage_fee, update_fee, usage_fee = calculate_total_fees(files, monthly_updates, max_storage_usage_mb)
    return f"UPDATE: {storage_fee} {update_fee} {usage_fee}"


def process_calc(files, monthly_updates, max_storage_usage_mb):
    """月次計算コマンドを処理"""
    # 各ストレージの使用量を取得（KB単位）
    storage_usage_list = []
    for storage_name in ["storage_A1", "storage_A2", "storage_B1", "storage_B2"]:
        total_kb = sum(files[storage_name].values()) if files[storage_name] else 0
        storage_usage_list.append(str(total_kb))

    # 月中の最大料金を計算
    max_storage_fee, max_update_fee, max_usage_fee = calculate_total_fees(files, monthly_updates, max_storage_usage_mb)

    # 月次更新量と最大利用量をリセット
    for storage_name in monthly_updates:
        monthly_updates[storage_name] = 0
    for storage_name in max_storage_usage_mb:
        max_storage_usage_mb[storage_name] = 0

    usage_info = " ".join(storage_usage_list)
    return f"CALC: [{usage_info}] {max_storage_fee} {max_update_fee} {max_usage_fee}"


def process_request_line(line, files, monthly_updates, max_storage_usage_mb):
    """1行のリクエストを解析して処理"""
    parts = line.strip().split()

    if len(parts) < 2:
        return "ERROR: Invalid request format"

    request_time = parts[0]
    command = parts[1]

    try:
        if command == "UPLOAD":
            if len(parts) != 5:
                return "ERROR: Invalid UPLOAD format"
            storage_name, filename, filesize_str = parts[2], parts[3], parts[4]
            filesize_kb = int(filesize_str)
            return process_upload(storage_name, filename, filesize_kb, files, monthly_updates,
                                          max_storage_usage_mb)

        elif command == "DELETE":
            if len(parts) != 4:
                return "ERROR: Invalid DELETE format"
            storage_name, filename = parts[2], parts[3]
            return process_delete(storage_name, filename, files, monthly_updates, max_storage_usage_mb)

        elif command == "UPDATE":
            if len(parts) != 5:
                return "ERROR: Invalid UPDATE format"
            storage_name, filename, filesize_str = parts[2], parts[3], parts[4]
            filesize_kb = int(filesize_str)
            return process_update(storage_name, filename, filesize_kb, files, monthly_updates,
                                          max_storage_usage_mb)

        elif command == "CALC":
            if len(parts) != 2:
                return "ERROR: Invalid CALC format"
            return process_calc(files, monthly_updates, max_storage_usage_mb)

        else:
            return f"ERROR: Unknown command: {command}"

    except ValueError as e:
        return f"ERROR: Invalid number format: {e}"
    except Exception as e:
        return f"ERROR: Unexpected error: {e}"


def initialize_storage_data():
    """ストレージデータを初期化"""
    files = {"storage_A1": {}, "storage_A2": {}, "storage_B1": {}, "storage_B2": {}}
    monthly_updates = {"storage_A1": 0, "storage_A2": 0, "storage_B1": 0, "storage_B2": 0}
    # 各ストレージの月中最大利用量を記録（MB単位）
    max_storage_usage_mb = {"storage_A1": 0, "storage_A2": 0, "storage_B1": 0, "storage_B2": 0}
    return files, monthly_updates, max_storage_usage_mb


def main(lines):
    
    files, monthly_updates, max_storage_usage_mb = initialize_storage_data()

    for line in lines:
        if line.strip():  
            result = process_request_line(line, files, monthly_updates, max_storage_usage_mb)
            print(result)


if __name__ == "__main__":
    
    lines = []
    for line in sys.stdin:
        lines.append(line.rstrip('\r\n'))

    main(lines)