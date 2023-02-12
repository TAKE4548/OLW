import tkinter as tk
from tkinter import ttk
from typing import Callable


class Window:
    """時計ウィンドウのオブジェクトセット

    Args:
        root (tk.Tk): ウィンドウルート
        menu (tk.Menu): コンテキストメニュー
        frame (ttk.Frame): オブジェクト配置フレーム
        time (ttk.Label): 時刻表示ラベル
        timevar (tk.StringVar): 時刻表示値更新用変数
        date (ttk.Label): 日付表示ラベル
        datevar (tk.StringVar): 日付表示値更新用変数
    """

    def __init__(
        self,
        root: tk.Tk,
        menu: tk.Menu,
        frame: ttk.Frame,
        time: ttk.Label,
        timevar: tk.StringVar,
        date: ttk.Label,
        datevar: tk.StringVar,
    ):
        self.__root = root
        self.__menu = menu
        self.__frame = frame
        self.__time = time
        self.__timevar = timevar
        self.__date = date
        self.__datevar = datevar
        self.__quit_funcs: list[Callable] = []

    @property
    def root(self) -> tk.Tk:
        return self.__root

    @property
    def menu(self) -> tk.Menu:
        return self.__menu

    @property
    def frame(self) -> ttk.Frame:
        return self.__frame

    @property
    def time(self) -> ttk.Label:
        return self.__time

    @property
    def timevar(self) -> tk.StringVar:
        return self.__timevar

    @property
    def date(self) -> ttk.Label:
        return self.__date

    @property
    def datevar(self) -> tk.StringVar:
        return self.__datevar

    def run(self):
        self.__root.mainloop()

    def close_window(self):
        """ウィンドウを閉じる時のハンドラ"""
        for func in self.__quit_funcs:
            func()
        self.root.destroy()

    def register_quit_procedure(self, func: Callable):
        """ウィンドウ閉じる前の終了処理関数を登録する

        Args:
            func (Callable): 終了処理関数
        """
        self.__quit_funcs.append(func)
