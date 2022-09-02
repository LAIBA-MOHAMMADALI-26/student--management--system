import pyodbc
from tkinter import *
from tkinter import messagebox


def register():

    con = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=E:\proj\Databaseproject1.accdb')
    cur = con.cursor()
    cur.execute("Select * from `teachers` WHERE `email` ='%s'" % email1.get())
    row = cur.fetchone()
    con.close()

    emaill = list(email1.get())

    if firstname.get() == "" or lastname.get()=="" or contact_no.get()=="" or email1.get()=="" or password1.get()=="":
         messagebox.showerror("Error ", "All fields are required to be fill")
    elif password1.get() != confirm_password1.get():
         messagebox.showerror("Error", "Password and confirm password should be same")
    elif "@" not in emaill:
         messagebox.showerror("error","Enter a valid email",parent=root)
    elif chick.get() == 0:
         messagebox.showerror("error", "Please Agree to our terms")
    elif row != None:
         messagebox.showerror("error", "Email already in use, try a different one",parent=root)
    else:
         try:
             con = pyodbc.connect(
                 r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=E:\proj\Databaseproject1.accdb')

             cur = con.cursor()
             cur.execute("INSERT INTO `teachers` (`firstname`,`lastname`,`contactno`,`email`,`password`) values('%s','%s','%s','%s','%s')" %(
                 firstname.get(),lastname.get(),contact_no.get(),email1.get(),password1.get()))
             messagebox.showinfo("Success","Registered succesfully",parent=root)
             con.commit()
             con.close()
             root.destroy()
             import login
         except Exception as e:
             messagebox.showerror("Error",f'Error due to {str(e)}',parent=root)


def signIn():
    root.destroy()
    import login


root = Tk()
root.title("REGISTRATIOIN")
root.geometry("1400x1400")


def terms():
    top = Toplevel()
    top.title("Terms and conditions")
    top.configure(background="pink")
    top.geometry("400x300")
    top.resizable(False, False)
    Label(top, text='''This is fake terms and conditions
         for student management.''', bg="pink", fg="black",font=('times new roman',20)).pack()
    Button(top, text="OK", command=top.destroy, bg="yellow", fg="red",width=5,height=2,font=('times new roman',10,'bold')).pack()



lastname = StringVar()
contact_no = StringVar()
email1 = StringVar()
password1 = StringVar()
confirm_password1 = StringVar()
firstname = StringVar()
chick = IntVar()

# -------------frame----------
leftLabel = Label(root, bg="#29A0A4")
rightLabel = Label(root, bg="#439AA9")
leftLabel.place(x=0, y=0, relheight=1, width=650)
rightLabel.place(x=650, y=0, relheight=1, relwidth=1)
f1 = Frame(root, bg="white")
f1.place(x=180, y=100, width=700, height=500)
tile = Label(f1, text="REGISTER HERE", font=("times new roman", 20, "bold"), bg="white", fg="green")
tile.place(x=50, y=10)
f_name = Label(f1, text="First name", font=("times new roman", 15, "bold"), bg="white", fg="grey")
f_name.place(x=50, y=60)
f_enter_name = Entry(f1, font=("times new roman", 15,), fg="black", bg="light gray", textvariable=firstname)
f_enter_name.place(x=50, y=100)
l_name = Label(f1, text="Last name", font=("times new roman", 15, "bold"), bg="white", fg="grey")
l_name.place(x=370, y=60)
enter_l_name = Entry(f1, font=("times new roman", 15,), fg="black", bg="light gray", textvariable=lastname)
enter_l_name.place(x=370, y=100)

# ----------row 1-------------
contact = Label(f1, text="Contact No.", font=("times new roman", 15, "bold"), bg="white", fg="grey")
contact.place(x=50, y=160)
contact_entry = Entry(f1, font=("times new roman", 15,), fg="black", bg="light gray", textvariable=contact_no)
contact_entry.place(x=50, y=200)
email = Label(f1, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="grey")
email.place(x=370, y=160)
email_entry = Entry(f1, font=("times new roman", 15), fg="black", bg="light gray", textvariable=email1)
email_entry.place(x=370, y=200)

# ----------row 2-------------
password = Label(f1, text=" Password", font=("times new roman", 15, "bold"), bg="white", fg="grey")
password.place(x=50, y=260)
enter_password = Entry(f1, font=("times new roman", 15), fg="black", bg="light gray", textvariable=password1)
enter_password.place(x=50, y=300)
confirm_password = Label(f1, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white", fg="grey")
confirm_password.place(x=370, y=260)
reenter_password = Entry(f1, font=("times new roman", 15,), fg="black", bg="light gray", textvariable=confirm_password1)
reenter_password.place(x=370, y=300)

# ---------------------row3---------------
chk = Checkbutton(f1, onvalue=1, offvalue=0, variable=chick).place(x=50, y=360)
Label(f1, text="I agree to the terms and conditions", font=("times new roman", 15, "italic"), fg="black",
      bg="white").place(x=78, y=360)

# -------------------terms----------------
but = Button(f1, text="REGISTER", command=register, cursor="hand2", font=("new times roman", 15, "bold"), bg="green")
but.place(x=450, y=360, width=200)
t = Button(f1, text="Terms and Conditions", command=terms, cursor="hand2", font=("new times roman", 15, "italic"),
           bg="white", fg="black", border=0).place(x=50, y=400)
Label(f1, text="Already has an account?", font=("new times roman", 10, "italic"), bg="white", fg="red", border=0).place(
    x=248, y=455)
button2 = Button(f1, text="Sign in", font=("new times roman", 15, "italic"), cursor="hand2", bg="white", fg="red",
                 border=0, command=signIn)
button2.place(x=400, y=445)

root.bind('<Return>',lambda event : register())


root.mainloop()