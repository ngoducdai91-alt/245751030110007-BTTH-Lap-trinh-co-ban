print("NGÔ ĐỨC ĐẠI")
print("msv:245751030110007")
import tkinter as tk
def create_radio_buttons():
    root = tk.Tk()
    root.title("Radio Buttons (Bài 5)")
    root.geometry('300x250')
    v = tk.IntVar()
    v.set(1) 
    languages = [
        ("Python", 1),
        ("Perl", 2),
        ("Java", 3),
        ("C++", 4),
        ("C", 5)
    ]
    def ShowChoice():
        print(f"Lựa chọn hiện tại (value): {v.get()}")
        status_label.configure(text=f"Đã chọn giá trị: {v.get()}")
    tk.Label(root,
             text="""Chọn ngôn ngữ lập trình yêu thích:""",
             justify=tk.LEFT,
             padx=20).pack(anchor=tk.W, pady=10)
    for text, val in languages:
        tk.Radiobutton(root,
                       text=text,
                       padx=20,
                       variable=v,
                       command=ShowChoice,
                       value=val).pack(anchor=tk.W)
    status_label = tk.Label(root, text=f"Đã chọn giá trị: {v.get()}", fg="blue")
    status_label.pack(pady=10)
    root_b = tk.Tk()
    root_b.title("Radio Buttons dạng nút bấm (Bài 5b)")
    root_b.geometry('300x250')
    v_b = tk.IntVar()
    v_b.set(1)
    tk.Label(root_b,
             text="""Chọn ngôn ngữ (dạng nút bấm):""",
             justify=tk.LEFT,
             padx=20).pack(anchor=tk.W, pady=10)
    for text, val in languages:
        tk.Radiobutton(root_b,
                       text=text,
                       indicatoron=0, 
                       width=20,
                       padx=20,
                       pady=5,
                       variable=v_b,
                       command=ShowChoice, 
                       value=val,
                       bg="lightgray",
                       selectcolor="lightblue").pack(anchor=tk.W)
    root.mainloop()
    root_b.mainloop()
if __name__ == "__main__":
    create_radio_buttons()
