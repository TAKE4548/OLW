import subprocess

from .point_manipulator import PointManipulator
from .size import Size


class PointManipulatorForLinux(PointManipulator):
    """Linux環境向けのウィンドウ表示位置の取得と設定機能を提供するクラス

    Args:
        target (tk.Tk): 参照・操作対象のウィンドウオブジェクト
    """

    def get_title_size(self) -> Size:
        size = self.get_size()
        size.height = self.__get_title_height()
        return size

    @staticmethod
    def __get_title_height() -> int:
        """タイトルバーの高さを取得する

        Returns:
            int: タイトルバーの高さ
        """
        cmd = "gsettings get org.gnome.desktop.wm.preferences button-layout"
        wm_name = subprocess.check_output(cmd, shell=True, universal_newlines=True).strip()

        # ウィンドウマネージャーごとにタイトルバーサイズを返す
        if wm_name == "appmenu:minimize,maximize,close":
            return 26  # Unity
        elif wm_name == "close:":
            return 30  # GNOME
        elif wm_name == "appmenu:minimize,maximize,close;":
            return 72  # Compiz (デフォルト)
        else:
            return 0  # タイトルバーなし
