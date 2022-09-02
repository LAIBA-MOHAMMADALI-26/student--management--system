
from tkinter import *
from tkinter import messagebox
import pyodbc

# Function for logging in 
def login():
    if emailEntry.get() == "" or passEntry.get() == "":
        messagebox.showerror("Error","Fill out all the boxes",parent=root)
    else:
        try:
            con = pyodbc.connect(
                r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=E:\proj\Databaseproject1.accdb')
            cur = con.cursor()
            cur.execute("SELECT * FROM `teachers` WHERE email='%s' and password='%s';" %(emailEntry.get(),passEntry.get()) )
            row = cur.fetchone()
            con.close()
            if row == None:
                messagebox.showerror("error","Invalid username or password",parent=root)
            else:
                root.destroy()
                import management
        except Exception as e:
            messagebox.showerror("Error",f"Error is {str(e)}", parent=root)



# Function to redirect to registration page
def register():
    root.destroy()
    import register

# Main window 
root = Tk()
root.title("LOGIN")
root.geometry("1400x1400")
# Background 
leftLabel = Label(root,bg="#6a12e6")
rightLabel = Label(root,bg="#1271e6")

leftLabel.place(x=0,y=0,relheight=1,width=650)
rightLabel.place(x=650,y=0,relheight=1,relwidth=1)

# Login Frame 
frame = Frame(root,bg="white")
frame.place(x=380,y=150,height=400,width=600)

# Labels 
titleLabel = Label(frame, text="LOGIN",font=("times new roman",35,"bold"),bg="white",fg="#1235e6")
titleLabel.place(x=250,y=40)

emailLabel = Label(frame,text="EMAIL ADDRESS", font=("times new roman",10,"bold"),bg="white",fg="#947c89")
emailLabel.place(x=120,y=100)

passLabel = Label(frame,text="PASSWORD", font=("times new roman",10,"bold"),bg="white",fg="#947c89")
passLabel.place(x=120,y=185)

askLabel = Label(frame, text = "Do not have an account?", font=("times new roman",10),bg="white",fg="#947c89")
askLabel.place(x=125,y=295,height=45,width=135)

# Entries 
emailEntry = Entry(frame,font=("arial",15),bg="lightgray")
emailEntry.place(x=120, y=120, width=350,height=35)

passEntry = Entry(frame, show="*", font=("arial",15),bg="lightgray")
passEntry.place(x=120,y=205,width=350,height=35)

# Buttons 
loginButton = Button(frame, text="LOGIN",font=("times new roman",26,"bold"),fg="white",bg="#e61287",cursor="hand2",command=login)
loginButton.place(x=150, y=255,width=200,height=40 )

regButton = Button(frame,text="Signup",font=("times new roman",14),bd=0,bg="white",fg="#e61287", cursor="hand2",command=register)
regButton.place(x=260,y=303)


root.bind('<Return>',lambda event : login())


root.mainloop()