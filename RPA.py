from tkinter import *
from tkinter import messagebox
import datetime
from tkinter import ttk
import sqlite3

# PDF Libraries
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus.tables import Table, TableStyle, colors

heading_font = ("Arial Bold", 45)
label_font = ("Arial Light", 20)
btn_font = ("Arial", 20)
btn_color = "#faf8bf"
label_bg = "#00569a"
entry_bg = "#FFFFFF"
label_fg = "black"
base_bg = "#FEFAE0"
entry_font = ("Arial", 18)
function_canvas_bg = "#FEFAE0"
btn_canvas_bg = "#fdffb6"
sub_heading_bg = "#fdffb6"
sub_heading_fg = "black"
fun_btn_fg = "black"
fun_btn_bg = "#FFFAFF"
fun_btn_fnt = ("Verdana", 14)
checkbtn_bg = "#FEFAE0"

checkbtn_font = ("Arial", 15)
small_lb_font = ("Arial", 18)
small_btn_font = ("Arial", 18)
textarea_font = ("Arial", 15)

# Creating Database
con = sqlite3.connect("class_db.db")
cur = con.cursor()
query = "CREATE TABLE IF NOT EXISTS courses(Course VARCHAR(30), Fees INT(11))"
cur.execute(query)
con.commit()

q = "select * from courses"
cur.execute(q)
course = cur.fetchall()
con.commit()

if len(course) == 0:
    subject_query = "INSERT INTO courses(Course, Fees) VALUES('C',1111), ('C++', 3100), ('Data Structures', 3500), ('DBMS', 3500), ('Java', 1000), ('Python', 1000), ('Advance Java', 3500)"
    cur.execute(subject_query)
    con.commit()

credentials_query = "CREATE TABLE IF NOT EXISTS credentials(username VARCHAR(30), password VARCHAR(30))"
cur.execute(credentials_query)
con.commit()

cred_q = "select * from credentials"
cur.execute(cred_q)
credentials = cur.fetchall()
con.commit()

if len(credentials) == 0:
    cred_query = "INSERT INTO credentials(username, password) VALUES('admin', 'admin')"
    cur.execute(cred_query)
    con.commit()

student_query = "CREATE TABLE IF NOT EXISTS student_data(name varchar(70), mobile varchar(10), gender varchar(10),total_fees int(10), paid_fees int(10), c int(10), cpp int(10), ds int(10), dbms int(10), java int(10), python int(10), advjava int(10), date varchar(30), remaining_fees int(10), second_date varchar(30), second_installment int(10))"
cur.execute(student_query)
con.commit()
con.close()
# Database creation complete

def main_base():
    base = Tk()
    base.title("Ravi Programming Academy")
    base.minsize(width=1000, height=700)
    base.geometry("1920x1080")
    base.configure(background="#FEFAE0")
    # icon_path = os.path.abspath("RPA-Logo-PNG.ico")
    # base.iconbitmap(icon_path)
    base.wm_state('zoomed')

    def dashboard():
        username = user_entry.get()
        password = pass_entry.get()

        con = sqlite3.connect("class_db.db")
        q = "select * from credentials where username='" + username + "'"
        cursor = con.cursor()
        cursor.execute(q)
        user_data = cursor.fetchall()
        con.commit()

        if len(user_data) > 0 and user_data[0][1] == password:
            login_canvas.destroy()

            def logout():
                all_student.destroy()
                girls.destroy()
                boys.destroy()
                btn1.destroy()
                btn2.destroy()
                btn3.destroy()
                btn4.destroy()
                btn5.destroy()
                btn6.destroy()
                btn7.destroy()
                logout.destroy()
                btn_canvas.destroy()
                function_canvas.destroy()
                login_page()
            
            # add student tab starts
            def add_student():
                add_student_canvas = Canvas(function_canvas, bg=function_canvas_bg)
                add_student_canvas.place(relx=0, rely=0, relwidth=1, relheight=1)

                con = sqlite3.connect("class_db.db")
                q = "select * from courses"
                cursor = con.cursor()
                cursor.execute(q)
                fees_ls = cursor.fetchall()
                con.commit()
                con.close()

                def calculate():
                    c = cvar.get()
                    cpp = cppvar.get()
                    ds = dsvar.get()
                    dbms = dbmsvar.get()
                    java = javavar.get()
                    python = pythonvar.get()
                    advjava = advjavavar.get()

                    paid_fees = int(fees_entry.get())

                    total_fees = c + cpp + ds + dbms + java + python + advjava
                    remaining_fees = total_fees - paid_fees
                        
                    total_fees_lb.configure(text="Total fees :" + "  " + str(total_fees))
                    remaining_fees_lb.configure(text="Remaining Fees :" + "  " + str(remaining_fees))

                def submit_data():
                    name = name_entry.get()
                    contact = contact_entry.get()
                    gender = var.get()
                    paid_fees = int(fees_entry.get())

                    con = sqlite3.connect("class_db.db")
                    q = "select * from student_data where mobile='" + contact + "'"
                    cursor = con.cursor()
                    cursor.execute(q)
                    student_found = cursor.fetchone()
                    con.commit()
                    print(student_found)

                    c = cvar.get()
                    cpp = cppvar.get()
                    ds = dsvar.get()
                    dbms = dbmsvar.get()
                    java = javavar.get()
                    python = pythonvar.get()
                    advjava = advjavavar.get()

                    d = datetime.datetime.today()
                    payment_date = str(d.day) + "/" + str(d.month) + "/" + str(d.year)

                    total_fees = c + cpp + ds + dbms + java + python + advjava
                    remaining_fees = total_fees - paid_fees

                    if student_found == None:
                        if name != "" and contact != "" and paid_fees != "" and len(contact) == 10:
                            query = "insert into student_data(name,mobile,gender,total_fees,paid_fees,c,cpp,ds,dbms,java,python,advjava,date,remaining_fees,second_installment) values('" + name + "','" + contact + "','" + gender + "'," + str(total_fees) + "," + str(paid_fees) + "," + str(c) + "," + str(cpp) + "," + str(ds) + "," + str(dbms) + "," + str(java) + "," + str(python) + "," + str(advjava) + ",'" + payment_date + "'," + str(remaining_fees) + "," + str(0) + ")"

                            con = sqlite3.connect("class_db.db")
                            cursor = con.cursor()
                            cursor.execute(query)
                            con.commit()
                            con.close()

                            messagebox.showinfo("Student Status", "Student Registered Successfully...")
                            
                        else:
                            messagebox.showerror("Student Status", "Data Not Added..!\nPlease Provide valid details.")
                    else:
                        messagebox.showerror("Student status", "Mobile number is already registered.")

                def reset_add_student():
                    name_entry.delete(0, END)
                    contact_entry.delete(0, END)
                    fees_entry.delete(0, END)
                    male.select()
                    total_fees_lb.configure(text="Total fees :" + "  " + "0")
                    remaining_fees_lb.configure(text="Remaining Fees :" + "  " + "0")

                    cvar.set(0)
                    cppvar.set(0)
                    dsvar.set(0)
                    dbmsvar.set(0)
                    javavar.set(0)
                    pythonvar.set(0)
                    advjavavar.set(0)

                heading_canvas = Canvas(add_student_canvas, bg=base_bg)
                heading_canvas.place(relx=0, rely=0, relwidth=1, relheight=0.1)

                heading = Label(heading_canvas, text="Add New Student", bg=sub_heading_bg, fg=sub_heading_fg, font=("Arial Bold", 30))
                heading.place(relwidth=1, relheight=0.99)

                name_lb = Label(add_student_canvas, text="Enter Student Name : ", font=small_lb_font, bg=base_bg, fg=label_fg)
                name_lb.place(relx=0.15, rely=0.15)

                name_entry = Entry(add_student_canvas, font=entry_font, bg=entry_bg)
                name_entry.place(relx=0.4, rely=0.152, relwidth=0.3, relheight=0.04)

                contact_lb = Label(add_student_canvas, text="Student Mobile no.   : ", font=small_lb_font, bg=base_bg, fg=label_fg)
                contact_lb.place(relx=0.15, rely=0.23)

                contact_entry = Entry(add_student_canvas, font=entry_font, bg=entry_bg)
                contact_entry.place(relx=0.4, rely=0.232, relwidth=0.3, relheight=0.04)

                gender_lb = Label(add_student_canvas, text="Gender : ", font=small_lb_font, bg=base_bg, fg=label_fg)
                gender_lb.place(relx=0.15, rely=0.31)

                var = StringVar(add_student_canvas)

                male = Radiobutton(add_student_canvas, text="Male", font=checkbtn_font, variable=var, value="male", bg=checkbtn_bg)
                male.place(relx=0.41, rely=0.31)
                male.select()

                female = Radiobutton(add_student_canvas, text="Female", font=checkbtn_font, variable=var, value="female", bg=checkbtn_bg)
                female.place(relx=0.51, rely=0.31)

                courses_lb = Label(add_student_canvas, text="Courses : ", font=small_lb_font, bg=base_bg, fg=label_fg)
                courses_lb.place(relx=0.15, rely=0.39)

                cvar = IntVar(add_student_canvas)
                cppvar = IntVar(add_student_canvas)
                dsvar = IntVar(add_student_canvas)
                dbmsvar = IntVar(add_student_canvas)
                javavar = IntVar(add_student_canvas)
                pythonvar = IntVar(add_student_canvas)
                advjavavar = IntVar(add_student_canvas)

                cvar.set(0)
                cppvar.set(0)
                dsvar.set(0)
                dbmsvar.set(0)
                javavar.set(0)
                pythonvar.set(0)
                advjavavar.set(0)

                c = Checkbutton(add_student_canvas, text="C", font=checkbtn_font, bg=checkbtn_bg, variable=cvar, onvalue=fees_ls[0][1], offvalue=0)
                c.place(relx=0.41, rely=0.39)

                cpp = Checkbutton(add_student_canvas, text="C++", font=checkbtn_font, bg=checkbtn_bg, variable=cppvar, onvalue=fees_ls[1][1], offvalue=0)
                cpp.place(relx=0.5, rely=0.39)

                data_structure = Checkbutton(add_student_canvas, text="Data Structures", bg=checkbtn_bg, font=checkbtn_font, variable=dsvar, onvalue=fees_ls[2][1], offvalue=0)
                data_structure.place(relx=0.6, rely=0.39)

                dbms = Checkbutton(add_student_canvas, text="DBMS", font=checkbtn_font, bg=checkbtn_bg, variable=dbmsvar, onvalue=fees_ls[3][1], offvalue=0)
                dbms.place(relx=0.78, rely=0.39)

                java = Checkbutton(add_student_canvas, text="Java", font=checkbtn_font, bg=checkbtn_bg, variable=javavar, onvalue=fees_ls[4][1], offvalue=0)
                java.place(relx=0.41, rely=0.47)

                python = Checkbutton(add_student_canvas, text="Python", font=checkbtn_font, bg=checkbtn_bg, variable=pythonvar, onvalue=fees_ls[5][1], offvalue=0)
                python.place(relx=0.5, rely=0.47)

                advjava = Checkbutton(add_student_canvas, text="Advance Java", font=checkbtn_font, bg=checkbtn_bg, variable=advjavavar, onvalue=fees_ls[6][1], offvalue=0)
                advjava.place(relx=0.6, rely=0.47)

                fees_lb = Label(add_student_canvas, text="Fees Paying :", font=small_lb_font, bg=base_bg, fg=label_fg)
                fees_lb.place(relx=0.15, rely=0.55)

                fees_entry = Entry(add_student_canvas, font=entry_font, bg=entry_bg)
                fees_entry.place(relx=0.4, rely=0.551, relwidth=0.3, relheight=0.04)

                calculate_btn = Button(add_student_canvas, text="Calculate", font=small_btn_font, bg="lightgreen", command=calculate)
                calculate_btn.place(relx=0.72, rely=0.551, relwidth=0.15, relheight=0.04)

                total_fees_lb = Label(add_student_canvas, text="Total fees :" + "  " + "0", bg=base_bg, font=small_lb_font, fg=label_fg)
                total_fees_lb.place(relx=0.44, rely=0.65)

                remaining_fees_lb = Label(add_student_canvas, text="Remaining Fees :" + "  " + "0", bg=base_bg, font=small_lb_font, fg=label_fg)
                remaining_fees_lb.place(relx=0.63, rely=0.65)

                submit = Button(add_student_canvas, text="Submit", font=small_btn_font, bg="lightgreen", command=submit_data)
                submit.place(relx=0.8, rely=0.155, relheight=0.04, relwidth=0.1)

                reset = Button(add_student_canvas, text="Reset", font=small_btn_font, bg="lightgreen", command=reset_add_student)
                reset.place(relx=0.8, rely=0.235, relheight=0.04, relwidth=0.1)
            # Add student tab ENDS Here

            # Pay fees tab starts Here
            def pay_fees(): 
                fees_pay_canvas = Canvas(function_canvas, bg=function_canvas_bg)
                fees_pay_canvas.place(relx=0, rely=0, relwidth=1, relheight=1)

                def get_details():
                    contact = contact_entry.get()

                    if len(contact) == 10:
                        con = sqlite3.connect("class_db.db")
                        q = "select * from student_data where mobile='" + contact + "'"
                        cursor = con.cursor()
                        cursor.execute(q)
                        fees_ls = cursor.fetchall()
                        con.commit()

                        if len(fees_ls) > 0:
                            remaining = fees_ls[0][13] 

                            fees_paid.configure(text="Fees Paid :" + "  " + (str(fees_ls[0][4] + fees_ls[0][15])))
                            remaining_fees.configure(text="Remaining fees :" + "  " + str(remaining))
                            name_lb.configure(text="Name : " + fees_ls[0][0])

                            if remaining == 0:
                                messagebox.showinfo("Fees status", "Student already paid all the fees...")
                            
                        else:
                            messagebox.showwarning("Mobile Number", "Sorry...\nNo such student details found...")
                        
                    else:
                        messagebox.showwarning("Mobile Number", "Please provide valid mobile number...")

                def add_fees():
                    contact = contact_entry.get()
                    con = sqlite3.connect("class_db.db")
                    q = "select * from student_data where mobile=" + contact
                    cursor = con.cursor()
                    cursor.execute(q)
                    fees_ls = cursor.fetchall()
                    con.commit()

                    remaining = fees_ls[0][13] - int(fees_entry.get())
                    updated_remaining_fees.configure(text="Updated remaining Fees :" + "  " + str(remaining))

                def update_fees():
                    contact = contact_entry.get()
                    con = sqlite3.connect("class_db.db")
                    q = "select * from student_data where mobile='" + contact + "'"
                    cursor = con.cursor()
                    cursor.execute(q)
                    fees_ls = cursor.fetchone()
                    con.commit()
                        
                    if len(contact) == 10 and len(fees_ls) > 0:
                        new_fees = int(fees_entry.get())

                        new_paid_fees = new_fees
                        d = datetime.datetime.today()
                        second_payment_date = str(d.day) + "/" + str(d.month) + "/" + str(d.year)

                        update_query = "update student_data set second_installment='" + str(new_paid_fees) + "'where mobile='" + contact + "'"
                        cursor = con.cursor()
                        cursor.execute(update_query)
                        con.commit()
                            
                        q = "select * from student_data where mobile='" + contact + "'"
                        cursor = con.cursor()
                        cursor.execute(q)
                        remaining_ls = cursor.fetchone()
                        con.commit()

                        new_remaining = remaining_ls[3] - (remaining_ls[4] + remaining_ls[15])
                        remaining_query = "update student_data set remaining_fees='" + str(new_remaining) + "'where mobile='" + contact + "'"
                        cursor = con.cursor()
                        cursor.execute(remaining_query)
                        con.commit()

                        date_query = "update student_data set second_date='" + str(second_payment_date) + "'where mobile='" + contact + "'"
                        cursor = con.cursor()
                        cursor.execute(date_query)
                        con.commit()
                            
                        con = sqlite3.connect("class_db.db")
                        q = "select * from student_data where mobile='" + contact + "'"
                        cursor = con.cursor()
                        cursor.execute(q)
                        fees_ls = cursor.fetchone()
                        con.commit()

                        remaining = fees_ls[13]
                        updated_remaining_fees.configure(text="Remaining Fees :" + "  " + str(remaining))

                        messagebox.showinfo("Fees Status", "Fees Updated Successfully...\nThank you")
                        
                    else:
                        messagebox.showwarning("Mobile Number", "Sorry...\nFees not updated, Try Again...")

                def reset_pay_fees():
                    contact_entry.delete(0, END)
                    fees_entry.delete(0, END)
                    fees_paid.configure(text="Fees Paid :" + "  " + "0")
                    remaining_fees.configure(text="Remaining fees :" + "  " + "0")
                    updated_remaining_fees.configure(text="Updated remaining Fees :" + "  " + "0")
                    name_lb.configure(text="Name : ")

                heading_canvas = Canvas(fees_pay_canvas, bg=base_bg)
                heading_canvas.place(relx=0, rely=0, relwidth=1, relheight=0.1)

                heading = Label(heading_canvas, text="Fees Collection", bg=sub_heading_bg, fg=sub_heading_fg, font=("Arial Bold", 30))
                heading.place(relwidth=1, relheight=0.99)

                contact_lb = Label(fees_pay_canvas, text="Student Mobile no.   : ", font=small_lb_font, bg=base_bg, fg=label_fg)
                contact_lb.place(relx=0.12, rely=0.15)

                contact_entry = Entry(fees_pay_canvas, font=entry_font, bg=entry_bg)
                contact_entry.place(relx=0.12, rely=0.23, relwidth=0.5, relheight=0.05)

                get_details_btn = Button(fees_pay_canvas, text="Get details", font=small_btn_font, bg="lightgreen", command=get_details)
                get_details_btn.place(relx=0.65, rely=0.23, relwidth=0.18, relheight=0.05)
                
                name_lb = Label(fees_pay_canvas, text="Name : ", bg=base_bg, font=small_lb_font, fg=label_fg)
                name_lb.place(relx=0.12, rely=0.33)

                fees_paid = Label(fees_pay_canvas, text="Fees Paid :" + "  " + "0", bg=base_bg, font=small_lb_font, fg=label_fg)
                fees_paid.place(relx=0.41, rely=0.33)

                remaining_fees = Label(fees_pay_canvas, text="Remaining fees :" + "  " + "0", bg=base_bg, font=small_lb_font, fg=label_fg)
                remaining_fees.place(relx=0.65, rely=0.33)

                fees_lb = Label(fees_pay_canvas, text="Fees Paying :", font=small_lb_font, bg=base_bg, fg=label_fg)
                fees_lb.place(relx=0.12, rely=0.43)

                fees_entry = Entry(fees_pay_canvas, font=entry_font, bg=entry_bg)
                fees_entry.place(relx=0.12, rely=0.51, relwidth=0.5, relheight=0.05)

                add_fees_btn = Button(fees_pay_canvas, text="Add", font=small_btn_font, bg="lightgreen", command=add_fees)
                add_fees_btn.place(relx=0.65, rely=0.51, relwidth=0.18, relheight=0.05)

                updated_remaining_fees = Label(fees_pay_canvas, text="Updated remaining Fees :" + "  " + "0", bg=base_bg, font=small_lb_font, fg=label_fg)
                updated_remaining_fees.place(relx=0.12, rely=0.6)

                submit = Button(fees_pay_canvas, text="Submit", font=small_btn_font, bg="lightgreen", command=update_fees)
                submit.place(relx=0.32, rely=0.69)

                reset = Button(fees_pay_canvas, text="Reset", font=small_btn_font, bg="lightgreen", command=reset_pay_fees)
                reset.place(relx=0.57, rely=0.69)
            # Pay fees tab ENDS Here
            
            # Student details tab Starts here
            def student_details():
                student_details_canvas = Canvas(function_canvas, bg=function_canvas_bg)
                student_details_canvas.place(relx=0, rely=0, relwidth=1, relheight=1)

                def get_details():
                    contact = contact_entry.get()
                    length = len(contact)
                    
                    if length==10:
                        con = sqlite3.connect("class_db.db")
                        query = "select * from student_data where mobile='" + contact + "'"
                        cursor = con.cursor()
                        cursor.execute(query)
                        student_data = cursor.fetchone()
                        con.commit()
                        con.close()

                        if student_data != None:
                            sub_array = []
                            
                            if student_data[5] > 0:
                                sub_array.append(" C ")
                            if student_data[6] > 0:
                                sub_array.append(" C++ ")
                            if student_data[7] > 0:
                                sub_array.append(" DS ")
                            if student_data[8] > 0:
                                sub_array.append(" DBMS ")
                            if student_data[9] > 0:
                                sub_array.append(" Java ")
                            if student_data[10] > 0:
                                sub_array.append(" Python ")
                            if student_data[11] > 0:
                                sub_array.append(" Adv. Java ")

                            sub_str = " ,".join(sub_array)

                            name.configure(text="Student Name :" + "  " + student_data[0])
                            mob_num.configure(text="Mobile Number :" + "  " + student_data[1])
                            fees_paid.configure(text="Fees paid :" + "  " + str(student_data[4] + student_data[15]))
                            remaining_fees.configure(text="Remaining Fees :" + "  " + str(student_data[13]))
                            courses.configure(text="Courses :" + "  " + str(sub_str))
                        
                        else:
                            messagebox.showerror("Student details", "No such student registered")
                    
                    else:
                        messagebox.showwarning("Mobile Number", "Please provide valid mobile number")

                def reset_student_details():
                    contact_entry.delete(0, END)
                    name.configure(text="Student Name :" + "  " + "0")
                    mob_num.configure(text="Mobile Number :" + "  " + "0")
                    fees_paid.configure(text="Fees paid :" + "  " + "0")
                    remaining_fees.configure(text="Remaining Fees :" + "  " + "0")
                    courses.configure(text="Courses :" + "  " + "0")

                heading_canvas = Canvas(student_details_canvas, bg=base_bg)
                heading_canvas.place(relx=0, rely=0, relwidth=1, relheight=0.1)

                heading = Label(heading_canvas, text="Student Details", bg=sub_heading_bg, fg=sub_heading_fg, font=("Arial Bold", 30))
                heading.place(relwidth=1, relheight=0.99)

                contact_lb = Label(student_details_canvas, text="Student Mobile no.   : ", font=small_lb_font, bg=base_bg, fg=label_fg)
                contact_lb.place(relx=0.15, rely=0.15)

                contact_entry = Entry(student_details_canvas, font=entry_font, bg=entry_bg)
                contact_entry.place(relx=0.15, rely=0.23, relwidth=0.4, relheight=0.05)

                get_details_btn = Button(student_details_canvas, text="Get details", font=small_btn_font, bg="lightgreen", command=get_details)
                get_details_btn.place(relx=0.6, rely=0.23, relwidth=0.18, relheight=0.05)

                name = Label(student_details_canvas, text="Student Name :" + "  " + "0", bg=base_bg, font=small_lb_font, fg=label_fg)
                name.place(relx=0.15, rely=0.35)

                mob_num = Label(student_details_canvas, text="Mobile Number :" + "  " + "0", bg=base_bg, font=small_lb_font, fg=label_fg)
                mob_num.place(relx=0.15, rely=0.43)

                fees_paid = Label(student_details_canvas, text="Fees paid :" + "  " + "0", font=small_lb_font, bg=base_bg, fg=label_fg)
                fees_paid.place(relx=0.15, rely=0.51)

                remaining_fees = Label(student_details_canvas, text="Remaining Fees :" + "  " + "0", bg=base_bg, font=small_lb_font, fg=label_fg)
                remaining_fees.place(relx=0.15, rely=0.59)

                courses = Label(student_details_canvas, text="Courses :" + "  " + "0", bg=base_bg, font=small_lb_font, fg=label_fg)
                courses.place(relx=0.15, rely=0.67)

                reset = Button(student_details_canvas, text="Reset", font=small_btn_font, bg="lightgreen", command=reset_student_details)
                reset.place(relx=0.66, rely=0.46, relheight=0.05)
            # Student details tab ENDS here

            # Payment details tab Starts here
            def payment_details():
                payment_details_canvas = Canvas(function_canvas, bg=function_canvas_bg)
                payment_details_canvas.place(relx=0, rely=0, relwidth=1, relheight=1)

                def get_payment_details():
                    contact = contact_entry.get()

                    if len(contact) == 10:
                        con = sqlite3.connect("class_db.db")
                        payment_query = "select * from student_data where mobile='" + contact + "'"
                        cursor = con.cursor()
                        cursor.execute(payment_query)
                        payment_data = cursor.fetchone()
                        con.commit()
                        con.close()

                        if payment_data != None:
                            sub_array = []
                            if payment_data[5] > 0:
                                sub_array.append(" C ")
                            if payment_data[6] > 0:
                                sub_array.append(" C++ ")
                            if payment_data[7] > 0:
                                sub_array.append(" DS ")
                            if payment_data[8] > 0:
                                sub_array.append(" DBMS ")
                            if payment_data[9] > 0:
                                sub_array.append(" Java ")
                            if payment_data[10] > 0:
                                sub_array.append(" Python ")
                            if payment_data[11] > 0:
                                sub_array.append(" Adv. Java ")

                            sub_str = " ,".join(sub_array)

                            name.configure(text="Student Name :" + "  " + payment_data[0])
                            courses.configure(text="Courses :" + "  " + str(sub_str))

                            for item in table.get_children():
                                table.delete(item)

                            table.insert("", "end", values=(payment_data[4], payment_data[12]))
                            table.insert("", "end", values=(payment_data[15], payment_data[14]))
                        
                        else:
                            messagebox.showerror("Payment details", "No such student data found")
                    
                    else:
                        messagebox.showwarning("Payment details", "Please provide valid mobile number")

                def reset_payment():
                    contact_entry.delete(0, END)
                    name.configure(text="Student Name :" + "  " + "0")
                    courses.configure(text="Courses :" + "  " + "0")
                    for item in table.get_children():
                        table.delete(item)

                heading_canvas = Canvas(payment_details_canvas, bg=base_bg)
                heading_canvas.place(relx=0, rely=0, relwidth=1, relheight=0.1)

                heading = Label(heading_canvas, text="Payment Details", bg=sub_heading_bg, fg=sub_heading_fg, font=("Arial Bold", 30))
                heading.place(relwidth=1, relheight=0.99)

                contact_lb = Label(payment_details_canvas, text="Student Mobile no.   : ", font=small_lb_font, bg=base_bg, fg=label_fg)
                contact_lb.place(relx=0.15, rely=0.15)

                contact_entry = Entry(payment_details_canvas, font=entry_font, bg=entry_bg)
                contact_entry.place(relx=0.15, rely=0.23, relwidth=0.4, relheight=0.05)

                get_details_btn = Button(payment_details_canvas, text="Get details", font=small_btn_font, bg="lightgreen", command=get_payment_details)
                get_details_btn.place(relx=0.6, rely=0.23, relwidth=0.18, relheight=0.05)

                name = Label(payment_details_canvas, text="Student Name :" + "  " + "0", bg=base_bg, font=small_lb_font, fg=label_fg)
                name.place(relx=0.15, rely=0.33)

                courses = Label(payment_details_canvas, text="Courses :" + "  " + "0", bg=base_bg, font=small_lb_font, fg=label_fg)
                courses.place(relx=0.15, rely=0.4)

                reset = Button(payment_details_canvas, text="Reset", font=small_btn_font, bg="lightgreen", command=reset_payment)
                reset.place(relx=0.661, rely=0.35)

                table_canvas = Canvas(payment_details_canvas, bg=entry_bg)
                table_canvas.place(relx=0.28, rely=0.5, relwidth=0.4, relheight=0.25)

                # Create a Treeview widget
                table = ttk.Treeview(table_canvas, columns=("Amount", "Date"), show="headings")
                table.place(relwidth=1, relheight=1)

                table.column(0, anchor=CENTER)
                table.column(1, anchor=CENTER)

                # Set the column headings
                table.heading(0, text="Amount")
                table.heading(1, text="Date")

                style = ttk.Style()
                style.theme_use("clam")
                style.configure("Treeview.Heading", font=(None, 15))
                style.configure(".", font=(None, 13))
            # Payment details tab ENDS here

            # Balance Fees tab Starts here
            def balance_fees():
                balance_fees_canvas = Canvas(function_canvas, bg=function_canvas_bg)
                balance_fees_canvas.place(relx=0, rely=0, relwidth=1, relheight=1)

                heading_canvas = Canvas(balance_fees_canvas, bg=base_bg)
                heading_canvas.place(relx=0, rely=0, relwidth=1, relheight=0.1)

                heading = Label(heading_canvas, text="Balance Fees", bg=sub_heading_bg, fg=sub_heading_fg, font=("Arial Bold", 30))
                heading.place(relwidth=1, relheight=0.99)

                contact_lb = Label(balance_fees_canvas, text="Select Subject   : ", font=small_lb_font, bg=base_bg, fg=label_fg)
                contact_lb.place(relx=0.18, rely=0.144)

                student_count = Label(heading_canvas, text="Students :" + "  " + "0", font=small_lb_font, bg=sub_heading_bg, fg=sub_heading_fg)
                student_count.place(relx=0.8, rely=0.3)

                canvas = Canvas(balance_fees_canvas, bg=base_bg)
                canvas.place(relx=0.4, rely=0.14, relwidth=0.2, relheight=0.05)

                courses = ["C", "C++", "Data Structures", "Python", "Java", "DBMS", "Advance Java"]
                var = StringVar(balance_fees_canvas)

                def getvalue(selection):
                    global subject
                    subject = var.get()

                def get_data():
                    if subject == "C":
                        con = sqlite3.connect("class_db.db")
                        q = "select * from student_data where c>0 and remaining_fees>0"
                        cursor = con.cursor()
                        cursor.execute(q)
                        all_data = cursor.fetchall()
                        con.commit()

                        con = sqlite3.connect("class_db.db")
                        query = "select name, mobile, paid_fees + second_installment, remaining_fees from student_data where c!=0 and remaining_fees>0"
                        cursor = con.cursor()
                        cursor.execute(query)
                        data = list(cursor.fetchall())

                        elements = []

                        # Add the main heading to the PDF
                        styles = getSampleStyleSheet()
                        elements.append(Paragraph("C - Remaining Fees", styles['Heading1']))

                        headings = ('Name', 'Mobile No.', 'Paid Fees', 'Remaining Fees')
                        data.insert(0, headings)

                        c_width = [2*inch, 2*inch, 1.5*inch, 1.5*inch]

                        my_doc = SimpleDocTemplate(filename = subject + ".pdf", pagesize=letter)
                        pdf_table = Table(data, rowHeights=30, colWidths=c_width, repeatRows=1)
                        pdf_table.setStyle(
                            TableStyle([
                                ('BACKGROUND', (0, 0), (-1, 0), colors.lightgreen),
                                ('FONTSIZE', (0, 0), (-1, -1), 12)
                            ])    
                        )

                        elements.append(pdf_table)
                        my_doc.build(elements)

                    if subject == "C++":
                        con = sqlite3.connect("class_db.db")
                        q = "select * from student_data where cpp>0 and remaining_fees>0"
                        cursor = con.cursor()
                        cursor.execute(q)
                        all_data = cursor.fetchall()
                        con.commit()

                        pdf_con = sqlite3.connect("class_db.db")
                        query = "select name, mobile, paid_fees + second_installment, remaining_fees from student_data where cpp!=0 and remaining_fees>0"
                        cursor = pdf_con.cursor()
                        cursor.execute(query)
                        data = list(cursor.fetchall())

                        elements = []

                        # Add the main heading to the PDF
                        styles = getSampleStyleSheet()
                        elements.append(Paragraph("C++ - Remaining Fees", styles['Heading1']))

                        headings = ('Name', 'Mobile No.', 'Paid Fees', 'Remaining Fees')
                        data.insert(0, headings)

                        c_width = [2*inch, 2*inch, 1.5*inch, 1.5*inch]

                        my_doc = SimpleDocTemplate(filename = subject + ".pdf", pagesize=letter)
                        pdf_table = Table(data, rowHeights=30, colWidths=c_width, repeatRows=1)
                        pdf_table.setStyle(
                            TableStyle([
                                ('BACKGROUND', (0, 0), (-1, 0), colors.lightgreen),
                                ('FONTSIZE', (0, 0), (-1, -1), 12)
                            ])    
                        )

                        elements.append(pdf_table)
                        my_doc.build(elements)

                    if subject == "Data Structures":
                        con = sqlite3.connect("class_db.db")
                        q = "select * from student_data where ds>0 and remaining_fees>0"
                        cursor = con.cursor()
                        cursor.execute(q)
                        all_data = cursor.fetchall()
                        con.commit()

                        pdf_con = sqlite3.connect("class_db.db")
                        query = "select name, mobile, paid_fees + second_installment, remaining_fees from student_data where ds!=0 and remaining_fees>0"
                        cursor = pdf_con.cursor()
                        cursor.execute(query)
                        data = list(cursor.fetchall())

                        elements = []

                        # Add the main heading to the PDF
                        styles = getSampleStyleSheet()
                        elements.append(Paragraph("Data Structures - Remaining Fees", styles['Heading1']))

                        headings = ('Name', 'Mobile No.', 'Paid Fees', 'Remaining Fees')
                        data.insert(0, headings)

                        c_width = [2*inch, 2*inch, 1.5*inch, 1.5*inch]

                        my_doc = SimpleDocTemplate(filename = subject + ".pdf", pagesize=letter)
                        pdf_table = Table(data, rowHeights=30, colWidths=c_width, repeatRows=1)
                        pdf_table.setStyle(
                            TableStyle([
                                ('BACKGROUND', (0, 0), (-1, 0), colors.lightgreen),
                                ('FONTSIZE', (0, 0), (-1, -1), 12)
                            ])    
                        )

                        elements.append(pdf_table)
                        my_doc.build(elements)

                    if subject == "Python":
                        con = sqlite3.connect("class_db.db")
                        q = "select * from student_data where python>0 and remaining_fees>0"
                        cursor = con.cursor()
                        cursor.execute(q)
                        all_data = cursor.fetchall()
                        con.commit()

                        con = sqlite3.connect("class_db.db")
                        query = "select name, mobile, paid_fees + second_installment, remaining_fees from student_data where python!=0 and remaining_fees>0"
                        cursor = con.cursor()
                        cursor.execute(query)
                        data = list(cursor.fetchall())

                        elements = []

                        # Add the main heading to the PDF
                        styles = getSampleStyleSheet()
                        elements.append(Paragraph("Python - Remaining Fees", styles['Heading1']))

                        headings = ('Name', 'Mobile No.', 'Paid Fees', 'Remaining Fees')
                        data.insert(0, headings)

                        c_width = [2*inch, 2*inch, 1.5*inch, 1.5*inch]

                        my_doc = SimpleDocTemplate(filename = subject + ".pdf", pagesize=letter)
                        pdf_table = Table(data, rowHeights=30, colWidths=c_width, repeatRows=1)
                        pdf_table.setStyle(
                            TableStyle([
                                ('BACKGROUND', (0, 0), (-1, 0), colors.lightgreen),
                                ('FONTSIZE', (0, 0), (-1, -1), 12)
                            ])    
                        )

                        elements.append(pdf_table)
                        my_doc.build(elements)
                        
                    if subject == "Java":
                        con = sqlite3.connect("class_db.db")
                        q = "select * from student_data where java>0 and remaining_fees>0"
                        cursor = con.cursor()
                        cursor.execute(q)
                        all_data = cursor.fetchall()
                        con.commit()

                        con = sqlite3.connect("class_db.db")
                        query = "select name, mobile, paid_fees + second_installment, remaining_fees from student_data where java!=0 and remaining_fees>0"
                        cursor = con.cursor()
                        cursor.execute(query)
                        data = list(cursor.fetchall())

                        elements = []

                        # Add the main heading to the PDF
                        styles = getSampleStyleSheet()
                        elements.append(Paragraph("Java - Remaining Fees", styles['Heading1']))

                        headings = ('Name', 'Mobile No.', 'Paid Fees', 'Remaining Fees')
                        data.insert(0, headings)

                        c_width = [2*inch, 2*inch, 1.5*inch, 1.5*inch]

                        my_doc = SimpleDocTemplate(filename = subject + ".pdf", pagesize=letter)
                        pdf_table = Table(data, rowHeights=30, colWidths=c_width, repeatRows=1)
                        pdf_table.setStyle(
                            TableStyle([
                                ('BACKGROUND', (0, 0), (-1, 0), colors.lightgreen),
                                ('FONTSIZE', (0, 0), (-1, -1), 12)
                            ])    
                        )

                        elements.append(pdf_table)
                        my_doc.build(elements) 
                        

                    if subject == "DBMS":
                        con = sqlite3.connect("class_db.db")
                        q = "select * from student_data where dbms>0 and remaining_fees>0"
                        cursor = con.cursor()
                        cursor.execute(q)
                        all_data = cursor.fetchall()
                        con.commit()

                        con = sqlite3.connect("class_db.db")
                        query = "select name, mobile, paid_fees + second_installment, remaining_fees from student_data where dbms!=0 and remaining_fees>0"
                        cursor = con.cursor()
                        cursor.execute(query)
                        data = list(cursor.fetchall())

                        elements = []

                        # Add the main heading to the PDF
                        styles = getSampleStyleSheet()
                        elements.append(Paragraph("DBMS - Remaining Fees", styles['Heading1']))

                        headings = ('Name', 'Mobile No.', 'Paid Fees', 'Remaining Fees')
                        data.insert(0, headings)

                        c_width = [2*inch, 2*inch, 1.5*inch, 1.5*inch]

                        my_doc = SimpleDocTemplate(filename = subject + ".pdf", pagesize=letter)
                        pdf_table = Table(data, rowHeights=30, colWidths=c_width, repeatRows=1)
                        pdf_table.setStyle(
                            TableStyle([
                                ('BACKGROUND', (0, 0), (-1, 0), colors.lightgreen),
                                ('FONTSIZE', (0, 0), (-1, -1), 12)
                            ])    
                        )

                        elements.append(pdf_table)
                        my_doc.build(elements)

                    if subject == "Advance Java":
                        con = sqlite3.connect("class_db.db")
                        q = "select * from student_data where advjava>0 and remaining_fees>0"
                        cursor = con.cursor()
                        cursor.execute(q)
                        all_data = cursor.fetchall()
                        con.commit()

                        con = sqlite3.connect("class_db.db")
                        query = "select name, mobile, paid_fees + second_installment, remaining_fees from student_data where advjava!=0 and remaining_fees>0"
                        cursor = con.cursor()
                        cursor.execute(query)
                        data = list(cursor.fetchall())

                        elements = []

                        # Add the main heading to the PDF
                        styles = getSampleStyleSheet()
                        elements.append(Paragraph("Advance Java - Remaining Fees", styles['Heading1']))

                        headings = ('Name', 'Mobile No.', 'Paid Fees', 'Remaining Fees')
                        data.insert(0, headings)

                        c_width = [2*inch, 2*inch, 1.5*inch, 1.5*inch]

                        my_doc = SimpleDocTemplate(filename = subject + ".pdf", pagesize=letter)
                        pdf_table = Table(data, rowHeights=30, colWidths=c_width, repeatRows=1)
                        pdf_table.setStyle(
                            TableStyle([
                                ('BACKGROUND', (0, 0), (-1, 0), colors.lightgreen),
                                ('FONTSIZE', (0, 0), (-1, -1), 12)
                            ])    
                        )

                        elements.append(pdf_table)
                        my_doc.build(elements)

                    student_count.configure(text="Students :" + "  " + str(len(all_data)))

                    for item in table.get_children():
                        table.delete(item)
                    
                    for eachline in all_data:
                        table.insert("", END, values=(eachline[0], eachline[4] + eachline[15], eachline[13]))

                dropdown = OptionMenu(canvas, var, *courses, command=getvalue)
                dropdown.place(relx=0, rely=0, relwidth=1, relheight=1)
                var.set("Select Course")

                get_details_btn = Button(balance_fees_canvas, text="Get details", font=small_btn_font, bg="lightgreen", command=get_data)
                get_details_btn.place(relx=0.65, rely=0.142, relwidth=0.13, relheight=0.05)

                table_canvas = Canvas(balance_fees_canvas, bg=entry_bg)
                table_canvas.place(relx=0.05, rely=0.22, relwidth=0.9, relheight=0.53)

                scroll = Scrollbar(balance_fees_canvas, orient='vertical')

                # Creating Table
                table = ttk.Treeview(table_canvas, columns=("Name", "Fees Paid", "Remaining Fees"), show="headings", yscrollcommand=scroll.set)
                table.place(relheight=1, relwidth=1)

                table.column(0, anchor=CENTER)
                table.column(1, anchor=CENTER)
                table.column(2, anchor=CENTER)

                table.heading(0, text="Name")
                table.heading(1, text="Fees Paid")
                table.heading(2, text="Remaining Fees")

                style = ttk.Style()
                style.theme_use("clam")
                style.configure("Treeview.Heading", font=("Helvetica", 15))
                style.configure(".", font=("Helvetica", 14), rowheight=35)

                scroll.place(relx=0.935, rely=0.262, relheight=0.487)
                scroll.config(command=table.yview)
            # Balance Fees tab ENDS here

            # Subject wise students tab Starts here
            def subject_wise_students():
                subject_wise_canvas = Canvas(function_canvas, bg=function_canvas_bg)
                subject_wise_canvas.place(relx=0, rely=0, relwidth=1, relheight=1)

                con = sqlite3.connect("class_db.db")

                heading_canvas = Canvas(subject_wise_canvas, bg=base_bg)
                heading_canvas.place(relx=0, rely=0, relwidth=1, relheight=0.1)

                heading = Label(heading_canvas, text="Subject Wise Students", bg=sub_heading_bg, fg=sub_heading_fg, font=("Arial Bold", 30))
                heading.place(relwidth=1, relheight=0.99)

                contact_lb = Label(subject_wise_canvas, text="Select Subject   : ", font=small_lb_font, bg=base_bg, fg=label_fg)
                contact_lb.place(relx=0.18, rely=0.144)

                student_count = Label(heading_canvas, text="Students :" + "  " + "0", font=small_lb_font, bg=sub_heading_bg, fg=sub_heading_fg)
                student_count.place(relx=0.8, rely=0.3)

                canvas = Canvas(subject_wise_canvas, bg=base_bg)
                canvas.place(relx=0.4, rely=0.14, relwidth=0.2, relheight=0.05)

                courses = ["C", "C++", "Data Structures", "Python", "Java", "DBMS", "Advance Java"]

                var = StringVar(subject_wise_canvas)

                def getvalue(selection):
                    global subject
                    subject = var.get()

                def get_data():
                    if subject == "C":
                        q = "select * from student_data where c>0"
                        cursor = con.cursor()
                        cursor.execute(q)
                        all_data = cursor.fetchall()
                        con.commit()

                    if subject == "C++":
                        q = "select * from student_data where cpp>0"
                        cursor = con.cursor()
                        cursor.execute(q)
                        all_data = cursor.fetchall()
                        con.commit()

                    if subject == "Data Structures":
                        q = "select * from student_data where ds>0"
                        cursor = con.cursor()
                        cursor.execute(q)
                        all_data = cursor.fetchall()
                        con.commit()

                    if subject == "Python":
                        q = "select * from student_data where python>0"
                        cursor = con.cursor()
                        cursor.execute(q)
                        all_data = cursor.fetchall()
                        con.commit()
                                                
                    if subject == "Java":
                        q = "select * from student_data where java>0"
                        cursor = con.cursor()
                        cursor.execute(q)
                        all_data = cursor.fetchall()
                        con.commit()
                                                
                    if subject == "DBMS":
                        q = "select * from student_data where dbms>0"
                        cursor = con.cursor()
                        cursor.execute(q)
                        all_data = cursor.fetchall()
                        con.commit()

                    if subject == "Advance Java":
                        q = "select * from student_data where advjava>0"
                        cursor = con.cursor()
                        cursor.execute(q)
                        all_data = cursor.fetchall()
                        con.commit()

                    student_count.configure(text="Students :" + "  " + str(len(all_data)))

                    for item in table.get_children():
                        table.delete(item)
                                                    
                    for eachline in all_data:
                        sub_array = []
                        if eachline[5] > 0:
                            sub_array.append(" C ")
                        if eachline[6] > 0:
                            sub_array.append(" C++ ")
                        if eachline[7] > 0:
                            sub_array.append(" DS ")
                        if eachline[8] > 0:
                            sub_array.append(" DBMS ")
                        if eachline[9] > 0:
                            sub_array.append(" Java ")
                        if eachline[10] > 0:
                            sub_array.append(" Python ")
                        if eachline[11] > 0:
                            sub_array.append(" Adv. Java ")

                        sub_str = " ,".join(sub_array)
                        
                        table.insert("", END, values=(eachline[0], eachline[1], sub_str))

                dropdown = OptionMenu(canvas, var, *courses, command=getvalue)
                dropdown.place(relx=0, rely=0, relwidth=1, relheight=1)
                var.set("Select Course")

                get_details_btn = Button(subject_wise_canvas, text="Get details", font=small_btn_font, bg="lightgreen", command=get_data)
                get_details_btn.place(relx=0.65, rely=0.142, relwidth=0.13, relheight=0.05)

                table_canvas = Canvas(subject_wise_canvas, bg=entry_bg)
                table_canvas.place(relx=0.05, rely=0.22, relwidth=0.9, relheight=0.53)

                scroll=Scrollbar(subject_wise_canvas, orient='vertical')

                # Creating Table
                table = ttk.Treeview(table_canvas, columns=("Name", "Mobile No.", "Courses"), show="headings", yscrollcommand=scroll.set)
                table.place(relheight=1, relwidth=1)

                table.column(0, anchor=CENTER)
                table.column(1, anchor=CENTER)
                table.column(2, anchor=CENTER)

                table.heading(0, text="Name")
                table.heading(1, text="Mobile No.")
                table.heading(2, text="Courses")

                style = ttk.Style()
                style.theme_use("clam")
                style.configure("Treeview.Heading", font=("Helvetica", 15))
                style.configure(".", font=("Helvetica", 14), rowheight=35)

                scroll.place(relx=0.935, rely=0.262, relheight=0.487)
                scroll.config(command=table.yview)
            # Subject Wise Students tab ENDS here

            # Update subject fees tab Starts here
            def update_subject_fees():
                update_fees_canvas = Canvas(function_canvas, bg=function_canvas_bg)
                update_fees_canvas.place(relx=0, rely=0, relwidth=1, relheight=1)

                def getvalue(selection):
                    global subject
                    subject = var.get()

                def update_fees():
                    up_fees = fees_entry.get()
                    con = sqlite3.connect("class_db.db")
                    q = "update courses set Fees="+ str(up_fees) + " where Course='" + subject + "'"
                    cursor = con.cursor()
                    cursor.execute(q)
                    con.commit()

                    query = "select * from courses"
                    cursor = con.cursor()
                    cursor.execute(query)
                    sub_data = cursor.fetchall()
                    con.commit()

                    for item in table.get_children():
                        table.delete(item)
                                                    
                    for eachline in sub_data:
                        table.insert("", END, values=(eachline[0], eachline[1]))
                        
                    messagebox.showinfo("Fees Status", "Subject fees updated successfully...")


                heading_canvas = Canvas(update_fees_canvas, bg=base_bg)
                heading_canvas.place(relx=0, rely=0, relwidth=1, relheight=0.1)

                heading = Label(heading_canvas, text="Update Subject Fees", bg=sub_heading_bg, fg=sub_heading_fg, font=("Arial Bold", 30))
                heading.place(relwidth=1, relheight=0.99)

                subject_lb = Label(update_fees_canvas, text="Select Subject   : ", font=small_lb_font, bg=base_bg, fg=label_fg)
                subject_lb.place(relx=0.15, rely=0.1495)

                canvas = Canvas(update_fees_canvas, bg=base_bg)
                canvas.place(relx=0.413, rely=0.144, relwidth=0.2, relheight=0.05)

                courses = ["C", "C++", "Data Structures", "Python", "Java", "DBMS", "Advance Java"]
                var = StringVar(update_fees_canvas)

                dropdown = OptionMenu(canvas, var, *courses, command=getvalue)
                dropdown.place(relx=0, rely=0, relwidth=1, relheight=1)
                var.set("Select Course")

                contact_lb = Label(update_fees_canvas, text="Enter Fees to Update :", font=small_lb_font, bg=base_bg, fg=label_fg)
                contact_lb.place(relx=0.15, rely=0.25)

                fees_entry = Entry(update_fees_canvas, font=entry_font, bg=entry_bg)
                fees_entry.place(relx=0.15, rely=0.32, relwidth=0.5, relheight=0.05)

                update_fees_btn = Button(update_fees_canvas, text="Update", font=small_btn_font, bg="lightgreen", command=update_fees)
                update_fees_btn.place(relx=0.7, rely=0.32, relwidth=0.18, relheight=0.05)

                table_canvas = Canvas(update_fees_canvas, bg=entry_bg)
                table_canvas.place(relx=0.21, rely=0.42, relwidth=0.6, relheight=0.34)

                # Creating Table
                table = ttk.Treeview(table_canvas, columns=("Subject", "Fees"), show="headings")
                table.place(relheight=1, relwidth=1)

                table.column(0, anchor=CENTER)
                table.column(1, anchor=CENTER)

                table.heading(0, text="Subject")
                table.heading(1, text="Fees")

                style = ttk.Style()
                style.theme_use("clam")
                style.configure("Treeview.Heading", font=("Helvetica", 15))
                style.configure(".", font=("Helvetica", 13), rowheight=35)

                con = sqlite3.connect("class_db.db")
                query = "select * from courses"
                cursor = con.cursor()
                cursor.execute(query)
                sub_data = cursor.fetchall()
                con.commit()
              
                for item in table.get_children():
                    table.delete(item)
                                                    
                for eachline in sub_data:
                    table.insert("", END, values=(eachline[0], eachline[1]))
            # Update subject fees tab ENDS here

            # All Student Query
            con = sqlite3.connect("class_db.db")
            query = "select * from student_data"
            cursor = con.cursor()
            cursor.execute(query)
            all_students = cursor.fetchall()
            con.commit()

            # Girls Query
            query = "select * from student_data where gender='female'"
            cursor = con.cursor()
            cursor.execute(query)
            girls_count = cursor.fetchall()
            con.commit()

            # Boys Query
            query = "select * from student_data where gender='male'"
            cursor = con.cursor()
            cursor.execute(query)
            boys_count = cursor.fetchall()
            con.commit()

            all_student = Label(heading_canvas, text="Students :" + "  " + str(len(all_students)), bg=base_bg, font=label_font, fg=label_fg)
            all_student.place(relx=0.01, rely=0.16)

            girls = Label(heading_canvas, text="Girls :" + "  " + str(len(girls_count)), bg=base_bg, font=label_font, fg=label_fg)
            girls.place(relx=0.01, rely=0.42)

            boys = Label(heading_canvas, text="Boys :" + "  " + str(len(boys_count)), bg=base_bg, font=label_font, fg=label_fg)
            boys.place(relx=0.01, rely=0.67)

            function_canvas = Canvas(base, bg=function_canvas_bg)
            function_canvas.place(relx=0.199, rely=0.198, relwidth=0.8, relheight=1)

            btn_canvas = Canvas(base, bg=btn_canvas_bg)
            btn_canvas.place(relx=0, rely=0.198, relwidth=0.2, relheight=1)

            # Calling first canvas by default
            add_student()

            # Adding Buttons to btn_canvas
            btn1 = Button(btn_canvas, text="Add Student (with fees)", bg=fun_btn_bg, fg=fun_btn_fg, font=fun_btn_fnt, command=add_student)
            btn1.place(relx=0, rely=0, relwidth=1, relheight=0.05)

            btn2 = Button(btn_canvas, text="Pay fees", bg=fun_btn_bg, fg=fun_btn_fg, font=fun_btn_fnt, command=pay_fees)
            btn2.place(relx=0, rely=0.05, relwidth=1, relheight=0.05)

            btn3 = Button(btn_canvas, text="Balance fees", bg=fun_btn_bg, fg=fun_btn_fg, font=fun_btn_fnt, command=balance_fees)
            btn3.place(relx=0, rely=0.1, relwidth=1, relheight=0.05)

            btn4 = Button(btn_canvas, text="Student details", bg=fun_btn_bg, fg=fun_btn_fg, font=fun_btn_fnt, command=student_details)
            btn4.place(relx=0, rely=0.15, relwidth=1, relheight=0.05)

            btn5 = Button(btn_canvas, text="Payment details", bg=fun_btn_bg, fg=fun_btn_fg, font=fun_btn_fnt, command=payment_details)
            btn5.place(relx=0, rely=0.2, relwidth=1, relheight=0.05)

            btn6 = Button(btn_canvas, text="Subject wise students", bg=fun_btn_bg, fg=fun_btn_fg, font=fun_btn_fnt, command=subject_wise_students)
            btn6.place(relx=0, rely=0.25, relwidth=1, relheight=0.05)

            btn7 = Button(btn_canvas, text="Update Subject Fees", bg=fun_btn_bg, fg=fun_btn_fg, font=fun_btn_fnt, command=update_subject_fees)
            btn7.place(relx=0, rely=0.3, relwidth=1, relheight=0.05)
            
            logout = Button(heading_canvas, text="Logout", bg=fun_btn_bg, fg=fun_btn_fg, font=fun_btn_fnt, command=logout)
            logout.place(relx=0.9, rely=0.37, relwidth=0.06, relheight=0.3)

        else:
            messagebox.showerror("Login Status", "Username or Password is wrong...\nPlease provide valid credentials.")


    heading_canvas = Canvas(base, bg="#FEFAE0")
    heading_canvas.place(relx=0, rely=0, relwidth=1, relheight=0.2)

    heading = Label(heading_canvas, text="Ravi Programming Academy", font=("Times New Roman", 60), bg=base_bg, fg="darkred")
    heading.place(relx=0.2, rely=0.14)
    # heading.place(relx=0.21, rely=0.25)

    def login_page():

        # Signup and Forgot Password window block variables
        signup_heading_font = ("Arial Bold", 45)
        signup_label_font = ("Arial Light", 20)
        signup_btn_font = ("Arial", 20)
        signup_label_bg = "#a5ffd6"
        signup_entry_bg = "#FFFFFF"
        signup_label_fg = "black"
        login_canvas_bg = "#a5ffd6"

        # Sign up window starts
        def sign_up_fun():
            login_canvas.destroy()

            def signup_cmd():
                username = user_entry.get()
                password = pass_entry.get()
                confirm_pass =  cpass_entry.get()
                pre_pass =  prepass_entry.get()

                con = sqlite3.connect("class_db.db")
                q = "select * from credentials where password='" + pre_pass + "'"
                cursor = con.cursor()
                cursor.execute(q)
                valid_pass = cursor.fetchall()
                con.commit()

                if len(valid_pass) > 0 and password == confirm_pass:
                    q = "insert into credentials values('" + username + "','" + password + "')"
                    cursor = con.cursor()
                    cursor.execute(q)
                    con.commit()

                    messagebox.showinfo("Signup Status", "New User Registered Successfully.")
                    signup_canvas.destroy()
                    login_page()
                
                else:
                    messagebox.showwarning("Signup Status", "Please Enter Confirm Password and Previous Password Correctly.")


            def cancel_signup():
                signup_canvas.destroy()
                login_page()

            signup_canvas = Canvas(base, background=login_canvas_bg)
            signup_canvas.place(relx=0.3, rely=0.215, relheight=0.75, relwidth=0.4)

            login_heading = Label(signup_canvas, text="Sign up", font=signup_heading_font, bg=signup_label_bg, fg=signup_label_fg)
            login_heading.place(relx=0.32, rely=0.1)

            user_label = Label(signup_canvas, text="Enter Username", font=signup_label_font, bg=signup_label_bg, fg=signup_label_fg)
            user_label.place(relx=0.05, rely=0.3)

            pass_label = Label(signup_canvas, text="Enter password", font=signup_label_font, bg=signup_label_bg, fg=signup_label_fg)
            pass_label.place(relx=0.05, rely=0.42)

            cpass_label = Label(signup_canvas, text="Confirm pass.", font=signup_label_font, bg=signup_label_bg, fg=signup_label_fg)
            cpass_label.place(relx=0.05, rely=0.54)

            prepass_label = Label(signup_canvas, text="Previous Pass.", font=signup_label_font, bg=signup_label_bg, fg=signup_label_fg)
            prepass_label.place(relx=0.05, rely=0.66)

            user_entry = Entry(signup_canvas, font=signup_label_font, bg=signup_entry_bg, border=1, highlightbackground="blue")
            user_entry.place(relx=0.45, rely=0.305, relwidth=0.5)

            pass_entry = Entry(signup_canvas, font=signup_label_font, bg=signup_entry_bg, border=1, highlightbackground="blue")
            pass_entry.place(relx=0.45, rely=0.425, relwidth=0.5)

            cpass_entry = Entry(signup_canvas, font=signup_label_font, bg=signup_entry_bg, border=1, highlightbackground="blue")
            cpass_entry.place(relx=0.45, rely=0.545, relwidth=0.5)

            prepass_entry = Entry(signup_canvas, font=signup_label_font, bg=signup_entry_bg, border=1, highlightbackground="blue")
            prepass_entry.place(relx=0.45, rely=0.665, relwidth=0.5)

            signup_btn = Button(signup_canvas, text="Sign up", font=signup_btn_font, bg=signup_entry_bg, command=signup_cmd)
            signup_btn.place(relx=0.29, rely=0.8)

            cancel_btn = Button(signup_canvas, text="Cancel", font=signup_btn_font, bg=signup_entry_bg, command=cancel_signup)
            cancel_btn.place(relx=0.6, rely=0.8)
        # Sign up window ends...

        # forgot password window starts here
        def change_pass():
            login_canvas.destroy()

            def reset_pass():
                username = user_entry.get()
                pre_pass = prepass_entry.get()
                new_pass = newpass_entry.get()

                con = sqlite3.connect("class_db.db")
                q = "select * from credentials where username='" + username + "'"
                cursor = con.cursor()
                cursor.execute(q)
                valid_user = cursor.fetchall()
                con.commit()

                if len(valid_user) > 0 and username == valid_user[0][0] and pre_pass == valid_user[0][1]:
                    q = "update credentials set password='" + new_pass + "' where username='" + username + "'"
                    cursor = con.cursor()
                    cursor.execute(q)
                    con.commit()
                    messagebox.showinfo("Password Status", "Password Changed Successfully.")
                    forgot_canvas.destroy()
                    login_page()

                else:
                    messagebox.showwarning("Password Status", "Please Enter Valid Credentials.")

            def cancel_forgot_base():
                forgot_canvas.destroy()
                login_page()

            forgot_canvas = Canvas(base, background=login_canvas_bg)
            forgot_canvas.place(relx=0.3, rely=0.215, relheight=0.75, relwidth=0.4)

            login_heading = Label(forgot_canvas, text="Recover Account", font=("Arial Bold", 35), bg=signup_label_bg, fg=signup_label_fg)
            login_heading.place(relx=0.195, rely=0.06)

            user_label = Label(forgot_canvas, text="Enter Username", font=signup_label_font, bg=signup_label_bg, fg=signup_label_fg)
            user_label.place(relx=0.1, rely=0.2)

            user_entry = Entry(forgot_canvas, font=signup_label_font, bg=signup_entry_bg, border=1, highlightbackground="blue")
            user_entry.place(relx=0.1, rely=0.29, relwidth=0.8)
                    
            prepass_label = Label(forgot_canvas, text="Enter Previous Password :", font=signup_label_font, bg=signup_label_bg, fg=signup_label_fg)
            prepass_label.place(relx=0.1, rely=0.4)

            prepass_entry = Entry(forgot_canvas, font=signup_label_font, bg=signup_entry_bg, border=1, highlightbackground="blue")
            prepass_entry.place(relx=0.1, rely=0.49, relwidth=0.8)

            newpass_label = Label(forgot_canvas, text="Enter New Password :", font=signup_label_font, bg=signup_label_bg, fg=signup_label_fg)
            newpass_label.place(relx=0.1, rely=0.6)

            newpass_entry = Entry(forgot_canvas, font=signup_label_font, bg=signup_entry_bg, border=1, highlightbackground="blue")
            newpass_entry.place(relx=0.1, rely=0.69, relwidth=0.8)

            reset_btn = Button(forgot_canvas, text="Reset", font=signup_btn_font, bg=signup_entry_bg, command=reset_pass)
            reset_btn.place(relx=0.29, rely=0.83)

            cancel_btn = Button(forgot_canvas, text="Cancel", font=signup_btn_font, bg=signup_entry_bg, command=cancel_forgot_base)
            cancel_btn.place(relx=0.6, rely=0.83)
        # forgot password window ends here

        global login_canvas
        login_canvas = Canvas(base, background=login_canvas_bg, border=2)
        login_canvas.place(relx=0.3, rely=0.215, relheight=0.75, relwidth=0.4)

        login_heading = Label(login_canvas, text="Login", font=heading_font, bg=signup_label_bg, fg=signup_label_fg)
        login_heading.place(relx=0.365, rely=0.05)

        user_label = Label(login_canvas, text="Enter Username", font=label_font, bg=signup_label_bg, fg=signup_label_fg)
        user_label.place(relx=0.1, rely=0.25)

        global user_entry
        user_entry = Entry(login_canvas, font=label_font, bg=entry_bg, border=1, highlightbackground="blue")
        user_entry.place(relx=0.1, rely=0.35, relwidth=0.8)

        pass_label = Label(login_canvas, text="Enter Password", font=label_font, bg=signup_label_bg, fg=signup_label_fg)
        pass_label.place(relx=0.1, rely=0.46)

        global pass_entry
        pass_entry = Entry(login_canvas, font=label_font, bg=entry_bg, show="*")
        pass_entry.place(relx=0.1, rely=0.56, relwidth=0.8)

        login_btn = Button(login_canvas, text="Login", font=btn_font, bg=entry_bg, command=dashboard)
        login_btn.place(relx=0.26, rely=0.71)

        signup_btn = Button(login_canvas, text="Sign up", font=btn_font, bg=entry_bg, command=sign_up_fun)
        signup_btn.place(relx=0.58, rely=0.71)

        forgot_btn = Button(login_canvas, text="Forgot Password?", font=("Arial",19), bg=signup_label_bg, fg=signup_label_fg, bd=0, command=change_pass)
        forgot_btn.place(relx=0.334, rely=0.83)
    
    login_page()
    base.mainloop()

main_base()