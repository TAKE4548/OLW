from ..window import Window
from .event_executer import DateObserver, TimeCounter, TimeObserver


class EventFactory:
    """イベントハンドラと各オブジェクトの紐づけを行う"""

    @staticmethod
    def create(window: Window):
        counter = TimeCounter()
        window.register_quit_procedure(counter.quit)
        observer = TimeObserver(window.timevar)
        counter.add_observer(observer)
        observer = DateObserver(window.datevar)
        counter.add_observer(observer)
