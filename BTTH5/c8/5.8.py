print("NGÔ ĐỨC ĐẠI")
print("msv:245751030110007")
import tkinter as tk

def create_personal_info_form():
    window = tk.Tk()
    window.title("Thông tin cá nhân")
    window.geometry('350x200')
    window.columnconfigure(1, weight=1) 
    tk.Label(window, text="Họ tên:").grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
    entry_name = tk.Entry(window)
    entry_name.grid(row=0, column=1, padx=10, pady=5, sticky=tk.EW)
    tk.Label(window, text="Ngày sinh:").grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
    entry_dob = tk.Entry(window)
    entry_dob.grid(row=1, column=1, padx=10, pady=5, sticky=tk.EW)
    tk.Label(window, text="MSSV:").grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
    entry_mssv = tk.Entry(window)
    entry_mssv.grid(row=2, column=1, padx=10, pady=5, sticky=tk.EW)
    tk.Label(window, text="Ngành học:").grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
    entry_major = tk.Entry(window)
    entry_major.grid(row=3, column=1, padx=10, pady=5, sticky=tk.EW)
    def submit_info():
        print(f"Thông tin đã nhập: {entry_name.get()}, {entry_mssv.get()}")   
    tk.Button(window, text="Submit", command=submit_info).grid(row=4, column=1, pady=10, sticky=tk.E)
    window.mainloop()
if __name__ == "__main__":
    create_personal_info_form()
    import tkinter as tk

def create_radio_button_form():
    root = tk.Tk()
    root.title("Lựa chọn Radio Button (Bài 8b)")
    root.geometry('300x200')
    v = tk.IntVar()
    v.set(1) 
    choices = [
        ("Lựa chọn 1", 1),
        ("Lựa chọn 2", 2),
        ("Lựa chọn 3", 3)
    ]
    result_label = tk.Label(root, text="Chưa có lựa chọn nào được xác nhận.", fg="blue")
    result_label.pack(pady=10)
    def on_click_me():
        current_choice_value = v.get()
        choice_text = next((text for text, val in choices if val == current_choice_value), "Không xác định")   
        message = f"Bạn đã chọn: {choice_text} (Giá trị: {current_choice_value})"
        result_label.configure(text=message, fg="red")
        print(message)
    for text, val in choices:
        tk.Radiobutton(root,
                       text=text,
                       padx=20,
                       variable=v,
                       value=val).pack(anchor=tk.W)
    click_button = tk.Button(root, text="Click Me", command=on_click_me)
    click_button.pack(pady=20)
    root.mainloop()
if __name__ == "__main__":
    create_radio_button_form()


