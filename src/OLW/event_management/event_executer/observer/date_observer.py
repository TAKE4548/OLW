import tkinter as tk
from datetime import datetime as dt
from datetime import timedelta as td

from .watch_observer import WatchObserver


class DateObserver(WatchObserver):
    """日付情報を更新するためのオブザーバー

    Args:
        target (tk.StringVar): 更新対象のオブジェクト
    """

    def __init__(self, target: tk.StringVar):
        super().__init__(target)
        self.__last_time: dt = dt.min

    def update(self, datetime: dt):
        """時刻情報を元に日付データを更新する

        Args:
            datetime (dt): 更新する時刻更新
        """
        if abs(datetime - self.__last_time) >= td(days=1):
            self._target.set(datetime.strftime('%Y/%m/%d %a'))