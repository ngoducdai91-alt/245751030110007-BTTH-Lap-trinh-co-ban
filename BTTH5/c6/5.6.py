print("NGÔ ĐỨC ĐẠI")
print("msv:245751030110007")
import tkinter as tk
def create_menu_window():

    window = tk.Tk()
    window.title("Ứng dụng Menu Tkinter (Bài 6)")
    window.geometry('400x300')
    def NewFile():
        print("Đã chọn 'New File!'")
        status_label.configure(text="Hành động: Tạo File Mới")
    def OpenFile():
        print("Đã chọn 'Open File!'")
        status_label.configure(text="Hành động: Mở File")
    def About():
        print("Đã chọn 'About'!")
        status_label.configure(text="Hành động: Giới thiệu")       
    def QuitApp():
        window.destroy() 
    menu_bar = tk.Menu(window)
    window.config(menu=menu_bar)
    file_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="New", command=NewFile)
    file_menu.add_command(label="Open...", command=OpenFile)
    file_menu.add_separator() 
    file_menu.add_command(label="Exit", command=QuitApp)
    menu_bar.add_cascade(label="File", menu=file_menu)
    help_menu = tk.Menu(menu_bar, tearoff=0)
    help_menu.add_command(label="About", command=About)
    menu_bar.add_cascade(label="Help", menu=help_menu)
    status_label = tk.Label(window, text="Sẵn sàng...", bd=1, relief=tk.SUNKEN, anchor=tk.W)
    status_label.pack(side=tk.BOTTOM, fill=tk.X)
    window.mainloop()
if __name__ == "__main__":
    create_menu_window()
