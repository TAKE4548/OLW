from src.OLW.event_management.event_executer import WindowCloser

from ...tkMock import TkMock


class Test_WindowCloser:
    """Windowを閉じるイベントハンドラのテスト"""

    @staticmethod
    def test_on_closingでウィンドウが閉じる():
        # 準備
        tk_root = TkMock()
        closer = WindowCloser(tk_root)
        is_called = False  # ポスト処理確認用フラグ

        def post_procedure_callback():
            nonlocal is_called
            is_called = True

        closer.register_quit_procedure(post_procedure_callback)

        # 実行
        closer.on_closing()

        # 検証
        assert tk_root.is_destroyed, "ウィンドウが閉じてない"
        assert is_called, "終了の前処理が実行されてない"
