import sys
import math
from datetime import datetime
from typing import Dict, List, Optional, Tuple


class Storage:
    """ストレージ情報を管理するクラス"""

    def __init__(self, name: str, storage_type: str, storage_price: float,
                 update_price: float, free_plan_available: bool):
        self.name = name
        self.storage_type = storage_type
        self.storage_price = storage_price
        self.update_price = update_price
        self.free_plan_available = free_plan_available


class File:
    """ファイル情報を管理するクラス"""

    def __init__(self, filename: str, size_kb: int):
        self.filename = filename
        self.size_kb = size_kb


class StorageService:
    """ストレージサービスの料金管理を行うメインクラス"""

    def __init__(self):
        self.storages = self._initialize_storages()
        self.stored_files: Dict[str, Dict[str, File]] = {
            'storage_A1': {},
            'storage_A2': {},
            'storage_B1': {},
            'storage_B2': {}
        }
        self.monthly_update_volume: Dict[str, int] = {
            'storage_A1': 0,
            'storage_A2': 0,
            'storage_B1': 0,
            'storage_B2': 0
        }

    def _initialize_storages(self) -> Dict[str, Storage]:
        """ストレージ情報を初期化"""
        return {
            'storage_A1': Storage('storage_A1', 'A', 0.01, 0.0005, True),
            'storage_A2': Storage('storage_A2', 'A', 0.001, 0.01, True),
            'storage_B1': Storage('storage_B1', 'B', 0.01, 0.001, False),
            'storage_B2': Storage('storage_B2', 'B', 0.0001, 0.5, False)
        }

    def _calculate_storage_usage_mb(self, storage_name: str) -> int:
        """指定ストレージの利用量をMB単位で計算（小数点以下切り上げ）"""
        total_kb = sum(file.size_kb for file in self.stored_files[storage_name].values())
        return math.ceil(total_kb / 1000) if total_kb > 0 else 0

    def _calculate_update_volume_mb(self, storage_name: str) -> int:
        """指定ストレージの更新量をMB単位で計算（小数点以下切り上げ）"""
        total_kb = self.monthly_update_volume[storage_name]
        return math.ceil(total_kb / 1000) if total_kb > 0 else 0

    def _calculate_storage_fee(self, storage_name: str, usage_mb: int) -> int:
        """保存料金を計算"""
        if usage_mb == 0:
            return 0
        storage = self.storages[storage_name]
        fee = usage_mb * storage.storage_price
        return math.ceil(fee)

    def _calculate_update_fee(self, storage_name: str, update_mb: int) -> int:
        """更新料金を計算"""
        if update_mb == 0:
            return 0
        storage = self.storages[storage_name]
        fee = update_mb * storage.update_price
        return math.ceil(fee)

    def _calculate_monthly_fees(self) -> Tuple[int, int, int]:
        """月次の総料金を計算"""
        total_storage_fee = 0
        total_update_fee = 0

        for storage_name in self.storages.keys():
            usage_mb = self._calculate_storage_usage_mb(storage_name)
            update_mb = self._calculate_update_volume_mb(storage_name)

            total_storage_fee += self._calculate_storage_fee(storage_name, usage_mb)
            total_update_fee += self._calculate_update_fee(storage_name, update_mb)

        usage_fee = max(0, total_storage_fee + total_update_fee - 1000)

        return total_storage_fee, total_update_fee, usage_fee

    def _check_free_plan_constraints(self, storage_name: str) -> Optional[str]:
        """無料プランの制約をチェック"""
        storage = self.storages[storage_name]

        # タイプBストレージは無料プランで利用不可
        if not storage.free_plan_available:
            return f"this storage location is not available on the free plan"

        return None

    def _check_fee_limit_constraint(self) -> bool:
        """料金制限をチェック（無料プランで0円を超える場合）"""
        _, _, usage_fee = self._calculate_monthly_fees()
        return usage_fee > 0

    def _format_fee_output(self, storage_fee: int, update_fee: int, usage_fee: int) -> str:
        """料金出力をフォーマット"""
        return f"{storage_fee} {update_fee} {usage_fee}"

    def process_upload_request(self, request_time: str, storage_name: str,
                               filename: str, filesize_kb: int) -> str:
        """アップロードリクエストを処理"""
        # 無料プランの制約チェック
        constraint_error = self._check_free_plan_constraints(storage_name)
        if constraint_error:
            return f"UPLOAD: {constraint_error}"

        # ファイルの重複チェック
        if filename in self.stored_files[storage_name]:
            return "UPLOAD: file already exists"

        # 仮想的にファイルを追加して料金制限をチェック
        self.stored_files[storage_name][filename] = File(filename, filesize_kb)

        if self._check_fee_limit_constraint():
            # 仮想追加を取り消し
            del self.stored_files[storage_name][filename]
            return "UPLOAD: free plan fee limit exceeded"

        # 成功時の処理
        storage_fee, update_fee, usage_fee = self._calculate_monthly_fees()
        return f"UPLOAD: {self._format_fee_output(storage_fee, update_fee, usage_fee)}"

    def process_delete_request(self, request_time: str, storage_name: str,
                               filename: str) -> str:
        """削除リクエストを処理"""
        # 無料プランの制約チェック
        constraint_error = self._check_free_plan_constraints(storage_name)
        if constraint_error:
            return f"DELETE: {constraint_error}"

        # ファイルの存在チェック
        if filename not in self.stored_files[storage_name]:
            return "DELETE: file does not exist"

        # 仮想的にファイルを削除して料金制限をチェック
        deleted_file = self.stored_files[storage_name][filename]
        del self.stored_files[storage_name][filename]

        if self._check_fee_limit_constraint():
            # 仮想削除を取り消し
            self.stored_files[storage_name][filename] = deleted_file
            return "DELETE: free plan fee limit exceeded"

        # 成功時の処理（削除は既に実行済み）
        storage_fee, update_fee, usage_fee = self._calculate_monthly_fees()
        return f"DELETE: {self._format_fee_output(storage_fee, update_fee, usage_fee)}"

    def process_update_request(self, request_time: str, storage_name: str,
                               filename: str, new_filesize_kb: int) -> str:
        """更新リクエストを処理"""
        # 無料プランの制約チェック
        constraint_error = self._check_free_plan_constraints(storage_name)
        if constraint_error:
            return f"UPDATE: {constraint_error}"

        # ファイルの存在チェック
        if filename not in self.stored_files[storage_name]:
            return "UPDATE: file does not exist"

        # 仮想的にファイルを更新して料金制限をチェック
        old_file = self.stored_files[storage_name][filename]
        self.stored_files[storage_name][filename] = File(filename, new_filesize_kb)
        self.monthly_update_volume[storage_name] += new_filesize_kb

        if self._check_fee_limit_constraint():
            # 仮想更新を取り消し
            self.stored_files[storage_name][filename] = old_file
            self.monthly_update_volume[storage_name] -= new_filesize_kb
            return "UPDATE: free plan fee limit exceeded"

        # 成功時の処理（更新は既に実行済み）
        storage_fee, update_fee, usage_fee = self._calculate_monthly_fees()
        return f"UPDATE: {self._format_fee_output(storage_fee, update_fee, usage_fee)}"

    def process_calc_command(self, command_time: str) -> str:
        """月次計算コマンドを処理"""
        # 各ストレージの利用量を取得（KB単位）
        storage_usages = []
        for storage_name in ['storage_A1', 'storage_A2', 'storage_B1', 'storage_B2']:
            total_kb = sum(file.size_kb for file in self.stored_files[storage_name].values())
            storage_usages.append(str(total_kb))

        # 月次料金を計算
        storage_fee, update_fee, usage_fee = self._calculate_monthly_fees()

        # 月次更新量をリセット
        for storage_name in self.monthly_update_volume:
            self.monthly_update_volume[storage_name] = 0

        usage_info = " ".join(storage_usages)
        fee_info = self._format_fee_output(storage_fee, update_fee, usage_fee)

        return f"CALC: {usage_info} {fee_info}"

    def process_request(self, line: str) -> str:
        """リクエスト行を解析して適切な処理を実行"""
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
                return self.process_upload_request(request_time, storage_name, filename, filesize_kb)

            elif command == "DELETE":
                if len(parts) != 4:
                    return "ERROR: Invalid DELETE format"
                storage_name, filename = parts[2], parts[3]
                return self.process_delete_request(request_time, storage_name, filename)

            elif command == "UPDATE":
                if len(parts) != 5:
                    return "ERROR: Invalid UPDATE format"
                storage_name, filename, filesize_str = parts[2], parts[3], parts[4]
                filesize_kb = int(filesize_str)
                return self.process_update_request(request_time, storage_name, filename, filesize_kb)

            elif command == "CALC":
                if len(parts) != 2:
                    return "ERROR: Invalid CALC format"
                return self.process_calc_command(request_time)

            else:
                return f"ERROR: Unknown command: {command}"

        except ValueError as e:
            return f"ERROR: Invalid number format: {e}"
        except Exception as e:
            return f"ERROR: Unexpected error: {e}"


def main(lines: List[str]) -> None:
    """メイン処理関数"""
    service = StorageService()

    for line in lines:
        if line.strip():  # 空行をスキップ
            result = service.process_request(line)
            print(result)


if __name__ == "__main__":
    # 標準入力から読み込み
    lines = []
    for line in sys.stdin:
        lines.append(line.rstrip('\r\n'))

    main(lines)