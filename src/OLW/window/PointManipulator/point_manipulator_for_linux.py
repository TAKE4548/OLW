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
        cmd = ['gsettings', 'get', 'org.gnome.desktop.wm.preferences', 'gtk-titlebar-height']
        try:
            titlebar_height = int(subprocess.check_output(cmd, stderr=subprocess.STDOUT).decode('utf-8').strip())
        except subprocess.CalledProcessError:
            cmd = ['gsettings', 'get', 'org.gnome.desktop.interface', 'font-name']
            font_size = subprocess.check_output(cmd).decode('utf-8').strip().strip("/'").split(' ')[-1]
            titlebar_height = int(font_size.split('@')[0]) + 18

        return titlebar_height
