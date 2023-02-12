import tkinter as tk

from ..event_executer import TitleVisibilitySwitcher
from .event_connector import EventConnector


class TitleVisibilitySwitchEvent(EventConnector):
    """タイトルバーの表示状態切り替えイベントを画面オブジェクトと紐付ける

    Args:
        menu (tk.Menu): コンテキストメニューのオブジェクト
        event (TitleVisibilitySwitcher): タイトルバー表示切り替えオブジェクト
    """

    def __init__(self, menu: tk.Menu, event: TitleVisibilitySwitcher):
        super().__init__(menu, event)
        self._executer: TitleVisibilitySwitcher
        self.__index: int = 0
        self.__register_menu()

    def __register_menu(self):
        """コンテキストメニューにタイトルバー表示切り替えを追加する

        Raises:
            ValueError: 想定外のラベルが設定されている時
        """
        msg = self.__select_msg()
        self._master.add_command(label=msg, command=self.event)
        index = self._master.index(msg)
        if index is None:
            raise ValueError
        self.__index = index

    def __select_msg(self) -> str:
        """現在の表示状態に対応したラベル文字列を返す

        Returns:
            str: メニューに表示するラベル文字列
        """
        if self._executer.is_hidden():
            return 'タイトルバーを表示'
        else:
            return 'タイトルバーを非表示'

    def event(self):
        """タイトルバー表示切替イベントのハンドラ"""
        if self._executer.is_hidden():
            self._executer.show()
        else:
            self._executer.hide()
        new_msg = self.__select_msg()
        self._master.entryconfigure(self.__index, label=new_msg)
