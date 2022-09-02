from tkinter import *
root = Tk()
root.title("STUDENT MANAGEMENT SYSTEM")
root.geometry("1400x1400")
def register():
    root.destroy()
    import register
def logIn():
    root.destroy()
    import login

# Background
leftLabel = Label(root,bg='aqua')
leftLabel.place(x=0,y=0,relheight=1,width=1400)
bg=PhotoImage(file=r'E:\j.png')
l1=Label(leftLabel,image=bg,bg='aqua').place(x=70,y=100,width=1300,height=600)
#REGISTER AND LOGIN BUTTON:
loginButton = Button(l1,command=logIn, text="LOGIN",font=("times new roman",40,"bold"),fg="white",bg="#0B8CB2",cursor="hand2")
loginButton.place(x=150, y=700,width=300,height=100)
register_but = Button(l1, text="REGISTER",cursor="hand2",command=register,font=("times new roman",40,"bold"),fg="white",bg="#0B8CB2")
register_but.place(x=1000, y=700,width=300,height=100)
#TOP TITLE:
lbl_title=Label(leftLabel,text='STUDENT MANAGEMENT SYSTEM',font=('times new roman',40,'bold'),fg='black',bg="#52BAC9")
lbl_title.place(x=0,y=0,width=1400,height=70)

root.mainloop()

