from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import * 

rw = Tk()
rw.title("Tic Tac Toe")
rw.geometry()

clicked = 0
count=0

def dis_btn():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

def won():
    

    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        
        messagebox.showinfo("Winner","Player with 'X' won the game!!")
        dis_btn()

    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        
        messagebox.showinfo("Winner","Player with 'X' won the game!!")
        dis_btn()

    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        
        messagebox.showinfo("Winner","Player with 'X' won the game!!")
        dis_btn()

    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        
        messagebox.showinfo("Winner","Player with 'X' won the game!!")
        dis_btn()

    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        
        messagebox.showinfo("Winner","Player with 'X' won the game!!")
        dis_btn()

    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        
        messagebox.showinfo("Winner","Player with 'X' won the game!!")
        dis_btn()

    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        
        messagebox.showinfo("Winner","Player with 'X' won the game!!")
        dis_btn()

    elif b7["text"] == "X" and b5["text"] == "X" and b3["text"] == "X":
        b7.config(bg="red")
        b5.config(bg="red")
        b3.config(bg="red")
        
        messagebox.showinfo("Winner","Player with 'X' won the game!!")
        dis_btn()

    elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        
        messagebox.showinfo("Winner","Player with 'O' won the game!!")
        dis_btn()

    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        
        messagebox.showinfo("Winner","Player with 'O' won the game!!")
        dis_btn()

    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        
        messagebox.showinfo("Winner","Player with 'O' won the game!!")
        dis_btn()

    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        
        messagebox.showinfo("Winner","Player with 'O' won the game!!")
        dis_btn()

    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        
        messagebox.showinfo("Winner","Player with 'O' won the game!!")
        dis_btn()

    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        
        messagebox.showinfo("Winner","Player with 'O' won the game!!")
        dis_btn()

    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        
        messagebox.showinfo("Winner","Player with 'O' won the game!!")
        dis_btn()

    elif b7["text"] == "O" and b5["text"] == "O" and b3["text"] == "O":
        b7.config(bg="red")
        b5.config(bg="red")
        b3.config(bg="red")
        
        messagebox.showinfo("Winner","Player with 'O' won the game!!")
        dis_btn()

    else:pass

    
def c(bt):
    global clicked, count

    if bt["text"] == "" and clicked==0:
        bt["text"] = "X"
        clicked=1
        count+=1
        won()

    elif bt["text"] == "" and clicked==1:
        bt["text"] = "O"
        clicked=0
        count+=1
        won()

    else: 
        messagebox.showerror("Tic Tac Toe","Box is already selected")



# 1
b1 = Button(rw, text="", bg="gray", width=10, height=5,command=lambda: c(b1))
b1.grid(row = 0, column= 0)

# 2
b2 = Button(rw, text="", bg="gray", width=10, height=5,command=lambda: c(b2))
b2.grid(row = 0, column= 1)

# 3
b3 = Button(rw, text="", bg="gray", width=10, height=5,command=lambda: c(b3))
b3.grid(row = 0, column= 2)

# 4
b4 = Button(rw, text="", bg="gray", width=10, height=5,command=lambda: c(b4))
b4.grid(row = 1, column= 0)

# 5
b5 = Button(rw, text="", bg="gray", width=10, height=5,command=lambda: c(b5))
b5.grid(row = 1, column= 1)

# 6
b6 = Button(rw, text="", bg="gray", width=10, height=5,command=lambda: c(b6))
b6.grid(row = 1, column= 2)

# 7
b7 = Button(rw, text="", bg="gray", width=10, height=5,command=lambda: c(b7))
b7.grid(row = 2, column= 0)

# 8
b8 = Button(rw, text="", bg="gray", width=10, height=5,command=lambda: c(b8))
b8.grid(row = 2, column= 1)

# 9
b9 = Button(rw, text="", bg="gray", width=10, height=5,command=lambda: c(b9))
b9.grid(row = 2, column= 2)



rw.mainloop()
