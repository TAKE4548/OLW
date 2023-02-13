import tkinter as tk

from .event_executer import EventExecuter


class TopmostSwitcher(EventExecuter):
    """ウィンドウの最前面表示を切り替える

    Args:
        target (tk.Tk): 対象のウィンドウ
    """

    def __init__(self, target: tk.Tk):
        super().__init__(target)
        self._target: tk.Tk

    def is_topmost(self) -> bool:
        """現在の設定状態を返す

        Returns:
            bool: True: 最前面固定中, False: 最前面固定解除
        """
        # ret = bool(self._target.attributes("-topmost"))
        # print(ret)
        return bool(self._target.attributes("-topmost"))

    def keep(self):
        """最前面固定にする"""
        self._target.attributes("-topmost", True)

    def release(self):
        """最前面固定を解除する"""
        self._target.attributes("-topmost", False)
