import pyodbc
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

m = Tk()

# all variables:
var_id = IntVar()
var_name = StringVar()
var_email = StringVar()
var_gender = StringVar()
var_rollno = StringVar()
var_batch = StringVar()
var_semester = StringVar()
var_phonenumber = StringVar()

# functions:(display,logout,delete,insert,reset):
def display():
    con = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=E:\proj\Databaseproject1.accdb')
    cursor = con.cursor()

    for i in student_table.get_children():
        student_table.delete(i)

    cursor.execute("select * from `student` ORDER BY `studentid` ASC")
    data = cursor.fetchall()
    if len(data) != 0:
        for i in data:
            student_table.insert("", END, values=i)

    con.close()

def insert():
    if (var_id.get() == "" or var_email.get() == ""):
        messagebox.showerror("ERROR", "ALL FIELDS ARE REQUIRED")

    else:
        try:
            con = pyodbc.connect(
                r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=E:\proj\Databaseproject1.accdb')

            cursor = con.cursor()
            cursor.execute(
                "INSERT INTO student (`studentid`, `studentname`, `email`,`gender`, `roll no`, `phone number`, `batch`, `semester`) values('%i','%s','%s','%s','%s','%s','%s','%s')" % (
                    var_id.get(),
                    var_name.get(),
                    var_email.get(),
                    var_gender.get(),
                    var_rollno.get(),
                    var_phonenumber.get(),
                    var_batch.get(),
                    var_semester.get()))

            con.commit()
            con.close()
            messagebox.showinfo("success", "student has been added", parent=m)
            for item in student_table.get_children():
                student_table.delete(item)
            display()
        except Exception as es:
            messagebox.showerror("error", f"due to:str{(es)}", parent=m)

def delete():
    con = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=E:\proj\Databaseproject1.accdb')

    cursor = con.cursor()
    if var_id.get() == "":
        messagebox.showerror("error", "Please enter a record to be deleted", parent=m)
    else:
        cursor.execute(f"DELETE FROM `student` WHERE `studentid` = {var_id.get()};")
        messagebox.showinfo("deleted", 'one record has been deleted')
    con.commit()
    con.close()
    reset()
    display()

def Logout():
    m.destroy()
    import main

def update():
    con = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=E:\proj\Databaseproject1.accdb')
    cursor = con.cursor()
    cursor.execute("SELECT * from `student` WHERE `studentid`= %i" %var_id.get())
    row = cursor.fetchone()

    if (var_id.get() == "" or var_email.get() == ""):
        messagebox.showerror("ERROR", "ID AND EMAIL ARE REQUIRED")
    elif row == None:
        messagebox.showerror("Error",f"Student with this student id {var_id.get()} doesnot exist",parent=m)
    else:
        try:
            con = pyodbc.connect(
                r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=E:\proj\Databaseproject1.accdb')
            cursor = con.cursor()
            cursor.execute(
                "UPDATE `student` SET `studentname` = '%s', `email`='%s', `gender`='%s', `roll no`='%s', `phone number`='%s', `batch`='%s', `semester`='%s' WHERE `studentid`=%i" % (
                var_name.get(), var_email.get(), var_gender.get(), var_rollno.get(), var_phonenumber.get(),
                var_batch.get(), var_semester.get(), var_id.get()))
            con.commit()
            con.close()
            messagebox.showinfo("updated", f"The record of student id : {var_id.get()} was updated", parent=m)
            display()
        except Exception as e:
            messagebox.showerror("Error", f"The error is {e}", parent=m)

def reset():
    var_id.set(0)
    var_name.set("")
    var_gender.set("")
    var_email.set("")
    var_rollno.set("")
    var_batch.set("")
    var_semester.set("")
    var_phonenumber.set("")
    for item in student_table.get_children():
        student_table.delete(item)

# main window:
m.geometry("1530x790+0+0")
m.title('STUDENT MANAGEMENT')

# label in main window:
lbl_title = Label(m, text='STUDENT MANAGEMENT SYSTEM', font=('times new roman', 20, 'bold'), fg='black', bg="aqua")
lbl_title.place(x=0, y=0, width=1530, height=70)

# log out button:
b7 = Button(lbl_title, text='LOGOUT', command=Logout, bg='black', fg='white', font=('times new roman', 16, 'bold'),
            width=10, height=30)
b7.pack(side=RIGHT)

# MAIN frame f1:
f1 = Frame(bd=2, relief=RIDGE, bg='gold')
f1.place(x=15, y=100, height=600, width=1530)

# left frame in main frame:
f2 = LabelFrame(f1, bd=4, relief=RIDGE, padx=2, bg='lightcoral', fg='midnight blue', text='STUDENT INFORMATION',
                font=('times new roman', 14, 'italic', 'underline'))
f2.place(x=10, y=10, width=660, height=900)

# labels and entries in left frame:
l1 = Label(f1, bg='lightcoral', bd=2)
l1.grid(row=2, column=1, padx=17)
l1 = Label(f1, font=('times new roman', 14, 'bold'), text='STUDENT ID', bg='yellow', bd=2, fg='BLACK', width=20,
           height=2)
l1.grid(row=3, column=1, padx=17, pady=12)
l2 = Label(f1, font=('times new roman', 14, 'bold'), text='NAME', bg='yellow', bd=2, fg='BLACK', width=20, height=2)
l2.grid(row=4, column=1, padx=12, pady=12)
l3 = Label(f1, font=('times new roman', 14, 'bold'), text='GENDER', bg='yellow', bd=2, fg='BLACK', width=20, height=2)
l3.grid(row=5, column=1, padx=12, pady=12)
l4 = Label(f1, font=('times new roman', 14, 'bold'), text='EMAIL', bg='yellow', bd=2, fg='BLACK', width=20, height=2)
l4.grid(row=6, column=1, padx=12, pady=12)
l5 = Label(f1, font=('times new roman', 14, 'bold'), text='ROLL NO', bg='yellow', bd=2, fg='BLACK', width=20, height=2)
l5.grid(row=7, column=1, padx=12, pady=12)
l6 = Label(f1, font=('times new roman', 14, 'bold'), text='PHONE NUMBER', bg='yellow', bd=2, fg='BLACK', width=20,
           height=2)
l6.grid(row=8, column=1, padx=12, pady=12)
l7 = Label(f1, font=('times new roman', 14, 'bold'), text='BATCH', bg='yellow', bd=2, fg='BLACK', width=20, height=2)
l7.grid(row=9, column=1, padx=12, pady=12)
l8 = Label(f1, font=('times new roman', 14, 'bold'), text='SEMESTER', bg='yellow', bd=2, fg='BLACK', width=20, height=2)
l8.grid(row=10, column=1, padx=12, pady=12)
e1 = ttk.Entry(f1, textvariable=var_id, width=15, font=('times new roman', 18))
e1.grid(row=3, column=2, pady=7)
e2 = ttk.Entry(f1, width=15, textvariable=var_name, font=('times new roman', 18))
e2.grid(row=4, column=2, pady=7)
e3 = ttk.Entry(f1, width=15, textvariable=var_gender, font=('times new roman', 18))
e3.grid(row=5, column=2, pady=7)
e4 = ttk.Entry(f1, width=15, textvariable=var_email, font=('times new roman', 18))
e4.grid(row=6, column=2, pady=7)
e5 = ttk.Entry(f1, width=15, textvariable=var_rollno, font=('times new roman', 18))
e5.grid(row=7, column=2, pady=7)
e6 = ttk.Entry(f1, width=15, textvariable=var_phonenumber, font=('times new roman', 18))
e6.grid(row=8, column=2, pady=7)
e7 = ttk.Entry(f1, width=15, textvariable=var_batch, font=('times new roman', 18))
e7.grid(row=9, column=2, pady=7)
e8 = ttk.Entry(f1, width=15, textvariable=var_semester, font=('times new roman', 18))
e8.grid(row=10, column=2, pady=7)

# right frame in main frame:
f3 = LabelFrame(f1, bd=4, relief=RIDGE, padx=2, bg='greenyellow', fg='midnight blue', text="STUDENT INFORMATION",
                font=('Times New Roman', 14, 'bold'))
f3.place(x=680, y=10, width=790, height=800)

# button frame in right frame:(display,delete,insert,reset)
search_frame = LabelFrame(f3, bd=4, relief=RIDGE, padx=2, text='search student information',
                          font=('times new roman', 12, 'bold'), bg='orange', fg='black')
search_frame.place(x=0, y=90, width=790, height=60)
b1 = Button(search_frame, text='DISPLAY', command=display, font=('times new roman', 14, 'bold'), bg='cyan', fg='black',
            width=12)
b1.grid(row=0, column=1, padx=2)
b2 = Button(search_frame, text='INSERT', command=insert, font=('times new roman', 14, 'bold'), bg='cyan', fg='black',
            width=12)
b2.grid(row=0, column=2, padx=2)
b3 = Button(search_frame, text='DELETE', command=delete, font=('times new roman', 14, 'bold'), bg='cyan', fg='black',
            width=12)
b3.grid(row=0, column=3, padx=2)
b6 = Button(search_frame, text='RESET', command=reset, font=('times new roman', 14, 'bold'), bg='cyan', fg='black',
            width=12, height=1)
b6.grid(row=0, column=4, padx=2)
b8 = Button(search_frame, text='UPDATE', command=update, font=('times new roman', 14, 'bold'), bg='cyan', fg='black',
            width=12, height=1)
b8.grid(row=0, column=5, padx=2)

# frame for tree view:
table_frame = Frame(f3, bd=4, relief=RIDGE, bg='deep sky blue')
table_frame.place(x=0, y=160, width=790, height=350)

# tree view scroll bars:
scroll_Y = ttk.Scrollbar(table_frame, orient=VERTICAL)
scroll_X = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
style = ttk.Style(table_frame)
style.configure("Treeview", background="light blue", fieldbackground="light blue", foreground="white")

# tree view(student_table):
student_table = ttk.Treeview(table_frame,
                             column=("id", "name", "email", "gender", "roll no", "phone number", "batch", "semester"),
                             yscrollcommand=scroll_Y.set, xscrollcommand=scroll_X.set)
scroll_Y.pack(side=RIGHT, fill=Y)
scroll_X.pack(side=BOTTOM, fill=X)
scroll_Y.config(command=student_table.yview)
scroll_X.config(command=student_table.xview)

# treeview headings and columns:
student_table.heading("id", text="ID", )
student_table.heading("name", text="NAME")
student_table.heading("email", text="EMAIL")
student_table.heading("gender", text="GENDER")
student_table.heading("roll no", text="ROLL NO")
student_table.heading("phone number", text="PHONENUMBER")
student_table.heading("batch", text="BATCH")
student_table.heading("semester", text="SEMESTER")
student_table.pack(fill=BOTH, expand=1)
student_table["show"] = "headings"
student_table.column("id", width=100)
student_table.column("name", width=100)
student_table.column("email", width=100)
student_table.column("gender", width=100)
student_table.column("phone number", width=100)
student_table.column("batch", width=100)
student_table.column("semester", width=100)
student_table.pack()
m.mainloop()