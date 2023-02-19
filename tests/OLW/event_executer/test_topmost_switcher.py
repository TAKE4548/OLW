from src.OLW.event_management.event_executer import TopmostSwitcher

from ...tkMock import TkMock


class Test_TopmostSwitcher:
    """最前面固定イベントハンドラのテスト"""

    @staticmethod
    def test_keep呼ぶと最前面固定になる():
        # 準備
        tk_root = TkMock()
        switcher = TopmostSwitcher(tk_root)

        # 実行
        switcher.keep()

        # 検証
        assert switcher.is_topmost(), "Switcherの管理フラグが最前面固定状態になってない"
        assert tk_root.find_attribute("-topmost"), "画面オプションの最前面固定が設定されてない"

    @staticmethod
    def test_release呼ぶと最前面固定が解除される():
        # 準備
        tk_root = TkMock()
        tk_root.attributes('-topmost', True)
        switcher = TopmostSwitcher(tk_root)

        # 実行
        switcher.release()

        # 検証
        assert not switcher.is_topmost(), "Switcherの管理フラグが解除状態になってない"
        assert not tk_root.find_attribute("-topmost"), "画面オプションの最前面固定が解除されてない"
