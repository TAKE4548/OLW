from ..window import Window
from .event_executer import TimeCounter, TimeObserver


class EventFactory:
    """イベントハンドラと各オブジェクトの紐づけを行う"""

    @staticmethod
    def create(window: Window):
        observer = TimeObserver(window.timevar)
        counter = TimeCounter()
        counter.add_observer(observer)
        window.register_quit_procedure(counter.quit)
