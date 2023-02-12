import tkinter as tk
from datetime import datetime as dt
from tkinter import font as tkfont
from tkinter import ttk

topmost: bool = False


def execute():
    global topmost
    topmost = not topmost
    root.attributes('-topmost', topmost)


root = tk.Tk()
root.title('tkinter application')
root.geometry('300x100')

font_time = tkfont.Font(family="M+ 1mn", size=34, weight='bold')
font_date = tkfont.Font(family="M+ 1mn", size=12)

frame = ttk.Frame(root)
frame.pack(fill=tk.BOTH)

# button_display = ttk.Button(frame, text='Window作成', command=display)
now = dt.now()
now_time = tk.StringVar(frame)
now_time.set(now.strftime('%H:%M:%S'))
now_date = tk.StringVar(frame)
now_date.set(now.strftime('%Y/%m/%d %a'))

time_label = ttk.Label(frame, textvariable=now_time, anchor='center', font=font_time)
date_label = ttk.Label(frame, textvariable=now_date, anchor='center', font=font_date)
time_label.pack(fill=tk.BOTH, expand=True, pady=(5, 0), padx=10)
date_label.pack(fill=tk.BOTH, expand=True, pady=(0, 5), padx=10)

# button_display.pack()

root.mainloop()
