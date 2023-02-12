import tkinter as tk
from tkinter import font as tkfont
from tkinter import ttk

from .events import MouseEvents
from .window import Window


class WindowFactory:
    """ウィンドウセットを作成するクラス"""

    @staticmethod
    def create() -> Window:
        root = tk.Tk()
        root.title('Resident watch')
        root.geometry('300x100')
        menu = tk.Menu(root, tearoff=0)
        root.bind(MouseEvents.RightClick, lambda e: menu.post(e.x_root, e.y_root))
        frame = ttk.Frame(root)
        frame.pack(fill=tk.BOTH)
        t_font = tkfont.Font(family="M+ 1mn", size=34, weight='bold')
        t_var = tk.StringVar(frame)
        time = ttk.Label(frame, textvariable=t_var, font=t_font)
        time.pack(fill=tk.BOTH, expand=True, pady=(5, 0), padx=10)
        d_font = tkfont.Font(family="M+ 1mn", size=12)
        d_var = tk.StringVar(frame)
        date = ttk.Label(frame, textvariable=d_var, font=d_font)
        date.pack(fill=tk.BOTH, expand=True, pady=(0, 5), padx=10)
        window = Window(root, menu, frame, time, t_var, date, d_var)
        root.protocol("WM_DELETE_WINDOW", window.close_window)
        return window
