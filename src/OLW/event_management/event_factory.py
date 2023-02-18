from ..window import Window
from .event_connector import TopmostSwitchEvent
from .event_executer import (DateObserver, TimeCounter, TimeObserver, TopmostSwitcher)


class EventFactory:
    """イベントハンドラと各オブジェクトの紐づけを行う"""

    @staticmethod
    def create(window: Window):
        # 定期実行イベント設定
        counter = TimeCounter()
        window.register_quit_procedure(counter.quit)
        observer = TimeObserver(window.timevar)
        counter.add_observer(observer)
        observer = DateObserver(window.datevar)
        counter.add_observer(observer)
        # コンテキストメニューのイベント設定
        executer = TopmostSwitcher(window.root)
        TopmostSwitchEvent(window.menu, executer)
