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

    def _select_msg(self) -> str:
        if self._executer.is_hidden():
            return 'タイトルバーを表示'
        else:
            return 'タイトルバーを非表示'

    def event(self):
        if self._executer.is_hidden():
            self._executer.show()
        else:
            self._executer.hide()
        new_msg = self._select_msg()
        self._master.entryconfigure(self._index, label=new_msg)
