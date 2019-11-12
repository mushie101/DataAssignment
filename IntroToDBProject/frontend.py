from tkinter import*
import tkinter.messagebox
import backend
sd = "0"
class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("Our database management system")
        self.root.geometry("1350x750+0+0")
        self.root.config(bg="cadet blue")

        StdID = StringVar()
        FirstName = StringVar()
        Surname = StringVar()
        DoB = StringVar()
        Age = StringVar()
        Gender = StringVar()
        Address = StringVar()
        Mobile = StringVar()
        #=====================================Auxilliary backend Functions=====================================
        def iExit():
            iExit = tkinter.messagebox.askyesno("Our database management system", "confirm if you want to exit")
            if iExit > 0:
                root.destroy()
            return
        
        def clearData():
            self.txtStdID.delete(0,END)
            self.txtFname.delete(0,END)
            self.txtSname.delete(0,END)
            self.txtDoB.delete(0,END)
            self.txtAge.delete(0,END)
            self.txtGender.delete(0,END)
            self.txtAddress.delete(0,END)
            self.txtMobile.delete(0,END)

        def addData():
            if(len(StdID.get())!=0):
                backend.addStudentRecord(StdID.get(), FirstName.get(), Surname.get(), DoB.get(), Age.get(), Gender.get(), Address.get(), Mobile.get())
                studentList.delete(0,END)
                studentList.insert(END, (StdID.get, FirstName.get(), Surname.get(), DoB.get(), Age.get(), Gender.get(), Address.get(), Mobile.get()))

        def displayData():
            studentList.delete(0, END)
            for row in backend.viewData():
                studentList.insert(END, row, str(""))

        def StudentRec(event):
            global sd
            searchStd = studentList.curselection()[0]
            sd = studentList.get(searchStd)

            self.txtStdID.delete(0,END)
            self.txtStdID.insert(END, sd[1])
            self.txtFname.delete(0,END)
            self.txtFname.insert(END, sd[2])
            self.txtSname.delete(0,END)
            self.txtSname.insert(END, sd[3])
            self.txtDoB.delete(0,END)
            self.txtDoB.insert(END, sd[4])
            self.txtAge.delete(0,END)
            self.txtAge.insert(END, sd[5])
            self.txtGender.delete(0,END)
            self.txtGender.insert(END, sd[6])
            self.txtAddress.delete(0,END)
            self.txtAddress.insert(END, sd[7])
            self.txtMobile.delete(0,END)
            self.txtMobile.insert(END, sd[8])
            
        def deleteData():
            if(len(StdID.get())!=0):
                backend.deleteRecord(sd[0])
                clearData()
                displayData()

        def searchDatabase():
            studentList.delete(0, END)
            for row in backend.searchData(StdID.get(), FirstName.get(), Surname.get(), DoB.get(), Age.get(), Gender.get(), Address.get(), Mobile.get()):
                studentList.insert(END,row,str(""))
        
        def update():
            if(len(StdID.get())!=0):
                backend.deleteRecord(sd[0])
                print(sd)
            if(len(StdID.get())!=0):
                backend.addStudentRecord(StdID.get(), FirstName.get(), Surname.get(), DoB.get(), Age.get(), Gender.get(), Address.get(), Mobile.get())
                studentList.delete(0, END)
                studentList.insert(END, (StdID.get(), FirstName.get(), Surname.get(), DoB.get(), Age.get(), Gender.get(), Address.get(), Mobile.get()))

        #=====================================Frames=====================================
        MainFrame = Frame(self.root, bg = "cadet blue")
        MainFrame.grid()

        TitleFrame = Frame(MainFrame,bd=2, padx=54,pady=8 ,bg = "Ghost White", relief = RIDGE)
        TitleFrame.pack(side=TOP)

        self.lblTitle = Label(TitleFrame, font=('arial', 47, 'bold'), text="Our Database Management System", bg="Ghost White")
        self.lblTitle.grid(sticky=W)

        ButtonFrame = Frame(MainFrame,bd=2,width = 1350, height = 70 ,padx=18,pady=10 ,bg = "cadet blue", relief = RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame,bd=1,width= 1300,height=400,padx=20,pady=20 ,bg = "cadet blue", relief = RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLeft = LabelFrame(DataFrame,bd=1,width= 1000,height=600,padx=20,bg = "Ghost White", relief = RIDGE, font=('arial', 20, 'bold'), text="Student Info")
        DataFrameLeft.pack(side=LEFT)

        DataFrameRight = LabelFrame(DataFrame,bd=1,width= 450,height=300,padx=31, pady=3,bg = "Ghost White", relief = RIDGE, font=('arial', 20, 'bold'), text="student Details")
        DataFrameRight.pack(side=RIGHT)

        #=====================================Labels and Entry Widget=====================================
        self.lblStdID = Label(DataFrameLeft, font=('arial',20, 'bold'), text="Student ID:",padx = 2, pady = 2,bg="Ghost White")
        self.lblStdID.grid(row=0,column=0,sticky=W)
        self.txtStdID = Entry(DataFrameLeft, font=('arial', 20, 'bold'), textvariable=StdID, width = 39)
        self.txtStdID.grid(row=0,column=1)

        self.lblFname = Label(DataFrameLeft, font=('arial',20, 'bold'), text="First name:",padx = 2, pady = 2,bg="Ghost White")
        self.lblFname.grid(row=1,column=0,sticky=W)
        self.txtFname = Entry(DataFrameLeft, font=('arial', 20, 'bold'), textvariable=FirstName, width = 39)
        self.txtFname.grid(row=1,column=1)

        self.lblSname = Label(DataFrameLeft, font=('arial',20, 'bold'), text="Surname:",padx = 2, pady = 2,bg="Ghost White")
        self.lblSname.grid(row=2,column=0,sticky=W)
        self.txtSname = Entry(DataFrameLeft, font=('arial', 20, 'bold'), textvariable=Surname, width = 39)
        self.txtSname.grid(row=2,column=1)

        self.lblDoB = Label(DataFrameLeft, font=('arial',20, 'bold'), text="Date of birth:",padx = 2, pady = 2,bg="Ghost White")
        self.lblDoB.grid(row=3,column=0,sticky=W)
        self.txtDoB = Entry(DataFrameLeft, font=('arial', 20, 'bold'), textvariable=DoB, width = 39)
        self.txtDoB.grid(row=3,column=1)

        self.lblAge = Label(DataFrameLeft, font=('arial',20, 'bold'), text="Age:",padx = 2, pady = 2,bg="Ghost White")
        self.lblAge.grid(row=4,column=0,sticky=W)
        self.txtAge = Entry(DataFrameLeft, font=('arial', 20, 'bold'), textvariable=Age, width = 39)
        self.txtAge.grid(row=4,column=1)

        self.lblGender = Label(DataFrameLeft, font=('arial',20, 'bold'), text="Gender:",padx = 2, pady = 2,bg="Ghost White")
        self.lblGender.grid(row=5,column=0,sticky=W)
        self.txtGender = Entry(DataFrameLeft, font=('arial', 20, 'bold'), textvariable=Gender, width = 39)
        self.txtGender.grid(row=5,column=1)

        self.lblAddress = Label(DataFrameLeft, font=('arial',20, 'bold'), text="Address:",padx = 2, pady = 3,bg="Ghost White")
        self.lblAddress.grid(row=6,column=0,sticky=W)
        self.txtAddress = Entry(DataFrameLeft, font=('arial', 20, 'bold'), textvariable=Address, width = 39)
        self.txtAddress.grid(row=6,column=1)

        self.lblMobile = Label(DataFrameLeft, font=('arial',20, 'bold'), text="Mobile:",padx = 2, pady = 3,bg="Ghost White")
        self.lblMobile.grid(row=7,column=0,sticky=W)
        self.txtMobile = Entry(DataFrameLeft, font=('arial', 20, 'bold'), textvariable=Mobile, width = 39)
        self.txtMobile.grid(row=7,column=1)
        
        #=====================================ListBox and ScrollBar Widget=====================================
        scrollbar = Scrollbar(DataFrameRight)
        scrollbar.grid(row = 0, column = 1, sticky='ns')

        studentList = Listbox(DataFrameRight, width=41, height=16, font=('ariel', 12, 'bold'), yscrollcommand=scrollbar.set)
        studentList.bind('<<ListboxSelect>>', StudentRec)
        studentList.grid(row = 0, column = 0, padx=8)
        scrollbar.config(command = studentList.yview)

        #=====================================Button Widget=====================================
        self.btnAddData = Button(ButtonFrame, text="Add New", font=('arial', 20, 'bold'), height = 1, width = 10, bd=4, command = addData)
        self.btnAddData.grid(row=0, column = 0)

        self.btnDisplayData = Button(ButtonFrame, text="Display", font=('arial', 20, 'bold'), height = 1, width = 10, bd=4, command=displayData)
        self.btnDisplayData.grid(row=0, column = 1)

        self.btnClearData = Button(ButtonFrame, text="Clear", font=('arial', 20, 'bold'), height = 1, width = 10, bd=4, command=clearData)
        self.btnClearData.grid(row=0, column = 2)

        self.btnDeleteData = Button(ButtonFrame, text="Delete", font=('arial', 20, 'bold'), height = 1, width = 10, bd=4, command=deleteData)
        self.btnDeleteData.grid(row=0, column = 3)

        self.btnSearchData = Button(ButtonFrame, text="Search", font=('arial', 20, 'bold'), height = 1, width = 10, bd=4, command=searchDatabase)
        self.btnSearchData.grid(row=0, column = 4)

        self.btnUpdateData = Button(ButtonFrame, text="Update", font=('arial', 20, 'bold'), height = 1, width = 10, bd=4, command= update)
        self.btnUpdateData.grid(row=0, column = 5)

        self.btnExit = Button(ButtonFrame, text="Exit", font=('arial', 20, 'bold'), height = 1, width = 10, bd=4, command=iExit)
        self.btnExit.grid(row=0, column = 6)

if __name__ == '__main__':
    root = Tk()
    application = Student(root)
    root.mainloop()
     