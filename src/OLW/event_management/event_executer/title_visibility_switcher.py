import tkinter as tk

from ...window import PointManipulatorForLinux
from .event_executer import EventExecuter


class TitleVisibilitySwitcher(EventExecuter):
    """タイトルバーの表示を切り替える

    Args:
        target (tk.Tk): 対象のウィンドウ
    """

    def __init__(self, target: tk.Tk):
        super().__init__(target)
        self._target: tk.Tk
        self._point_manipulator = PointManipulatorForLinux(self._target)

    def is_hidden(self) -> bool:
        """現在の表示状態を返す

        Returns:
            bool: True: 非表示, False: 表示
        """
        ret = self._target.overrideredirect(None)
        return ret is not None

    def hide(self):
        """タイトルバーを非表示にする"""
        self.__switch(True)

    def show(self):
        """タイトルバーを表示する"""
        self.__switch(False)

    def __switch(self, mode: bool):
        """タイトルバーの表示状態を切り替える

        Args:
            mode (bool): True: 非表示, False: 表示
        """
        point = self._point_manipulator.get_point()
        print(mode)
        print(point)
        # 非表示にする時はタイトルバーの高さ分現在値より下にずらす
        if mode:
            title_bar_size = self._point_manipulator.get_title_size()
            point.offset(y=title_bar_size.height)
        self._target.overrideredirect(mode)
        self._target.geometry(point.for_geometry())
        self._target.update()
        # self._target.withdraw()
        # self._target.deiconify()
        print(self._point_manipulator.get_point())
        print('-' * 80)
