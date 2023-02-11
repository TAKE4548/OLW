import tkinter as tk
from tkinter import ttk

topmost: bool = False


def execute():
    global topmost
    topmost = not topmost
    root.attributes('-topmost', topmost)


def display():
    app = tk.Tk()
    app.title("hoge")
    app.geometry("300x100")

    frame_app = ttk.Frame(app)
    frame_app.pack(fill=tk.BOTH, pady=10)

    button_execute = ttk.Button(frame_app, text='fuga', command=execute)

    button_execute.pack()

    app.mainloop()


root = tk.Tk()
root.title('tkinter application')
root.geometry('300x100')

frame = ttk.Frame(root)
frame.pack(fill=tk.BOTH, pady=10)

button_display = ttk.Button(frame, text='Window作成', command=display)

button_display.pack()

root.mainloop()
