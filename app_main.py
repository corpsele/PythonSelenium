import tkinter as tk
from tkinter import messagebox

def change_label_text():
    new_text = entry.get()
    label.config(text=new_text)

def show_input():
    input_text = entry.get()
    messagebox.showinfo("输入内容", input_text)

def exit_app():
    root.destroy()

def show_root():
    global root
    global entry
    global label
    # 创建主窗口
    root = tk.Tk()
    root.title("Tkinter 多功能示例")

    # 设置窗口大小
    root.geometry("300x200")

    # 添加一个标签
    label = tk.Label(root, text="Hello, Tkinter!")
    label.pack(pady=10)

    # 添加一个文本输入框
    entry = tk.Entry(root)
    entry.pack(pady=10)

    # 添加一个按钮，用于更改标签文本
    button_change = tk.Button(root, text="更改标签文本", command=change_label_text)
    button_change.pack(pady=5)

    # 添加一个按钮，用于显示输入框内容
    button_show = tk.Button(root, text="显示输入内容", command=show_input)
    button_show.pack(pady=5)

    # 添加一个按钮，用于退出应用程序
    button_exit = tk.Button(root, text="退出", command=exit_app)
    button_exit.pack(pady=5)

    # 运行主循环
    root.mainloop()
