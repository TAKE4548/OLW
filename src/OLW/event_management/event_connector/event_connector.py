import tkinter as tk
from abc import ABC

from ..event_executer import EventExecuter


class EventConnector(ABC):
    """コンテキストメニューとイベントを紐付ける基底クラス

    Args:
        menu (tk.Menu): コンテキストメニューのオブジェクト
        event (EventExecuter): 紐付けるイベントの処理を持つオブジェクト
    """

    def __init__(self, menu: tk.Menu, event: EventExecuter):
        self._master = menu
        self._executer = event
