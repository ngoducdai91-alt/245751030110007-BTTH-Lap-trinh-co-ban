print("NGÔ ĐỨC ĐẠI")
print("msv:245751030110007")
import tkinter 
import random 
colours = ['Red','Blue','Green','Pink','Black', 
'Yellow','Orange','White','Purple','Brown'] 
score = 0
timeleft = 120 
def startGame(event): 
    if timeleft == 120:  
        countdown() 
    nextColour()  
def nextColour(): 
    global score 
    global timeleft 
    if timeleft > 0:  
        e.focus_set() 
        user_input = e.get().lower()
        correct_color_of_text = colours[1].lower() 
        if user_input == correct_color_of_text: 
            score += 2
        elif user_input != "" :
            score -= 1 
        e.delete(0, tkinter.END) 
        random.shuffle(colours) 
        label.config(fg = str(colours[1]), text = str(colours[0])) 

        scoreLabel.config(text = "Score: " + str(score))  
def countdown(): 
    global timeleft 
    if timeleft > 0: 
        timeleft -= 1
        timeLabel.config(text = "Time left: " + str(timeleft)) 
        timeLabel.after(1000, countdown)
    else:
        label.config(text="HẾT GIỜ!", fg="black")
root = tkinter.Tk() 
root.title("COLORGAME") 
root.geometry("375x250")  
instructions = tkinter.Label(root, text = "Gõ MÀU SẮC của chữ, không phải từ ngữ!", 
font = ('Helvetica', 12)) 
instructions.pack() 
scoreLabel = tkinter.Label(root, text = "Nhấn Enter để bắt đầu", 
font = ('Helvetica', 12)) 
scoreLabel.pack() 
timeLabel = tkinter.Label(root, text = "Time left: " + str(timeleft), font = ('Helvetica', 12)) 
timeLabel.pack() 
label = tkinter.Label(root, font = ('Helvetica', 60)) 
label.pack() 
e = tkinter.Entry(root)  
root.bind('<Return>', startGame) 
e.pack()  
e.focus_set() 
root.mainloop()
