"""
from tkinter import *
import time
import ttkthemes
from tkinter import ttk,messagebox,filedialog
import pymysql
import pandas


root=Tk()
root.mainloop()

#functionality part
def exit_data():
    result=messagebox.askyesno('Confirm','Do you want to exit?')
    if result:
        root.destroy()
    else:
        pass



def export_data():
    url=filedialog.asksaveasfilename(defaultextension='.csv')
    indexing=LibraryTable.get_children()
    newlist=[]
    for index in indexing:
        content=LibraryTable.item(index)
        datalist=content['values']
        newlist.append(datalist)


    table=pandas.DataFrame(newlist,columns=['ADD BOOK','VIEW BOOK','ISSUE BOOK ','RETURN BOOK','SEARCH BOOK'])
    table.to_csv(url,index=False)
    messagebox.showinfo('Success','Data is save Successfully')

def toplevel_data(title, button_text, command):
    global ADDBOOKEntry, VIEWBOOKEntry, ISSUEBOOKEntry, RETURNBOOKEntry, SEARCHBOOKEntry, screen

    screen = Toplevel()
    screen.title(title)
    screen.grab_set()
    screen.resizable(0, 0)

    ADDBOOKLabel = Label(screen, text='Name', font=('times new roman', 20, 'bold'))
    ADDBOOKLabel.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    ADDBOOKEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    ADDBOOKEntry.grid(row=1, column=1, pady=15, padx=10)

    VIEWBOOKLabel = Label(screen, text='Email', font=('times new roman', 20, 'bold'))
    VIEWBOOKLabel.grid(row=2, column=0, padx=30, pady=15, sticky=W)
    VIEWBOOKEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    VIEWBOOKEntry.grid(row=2, column=1, pady=15, padx=10)

    ISSUESLabel = Label(screen, text='Mobile', font=('times new roman', 20, 'bold'))
    ISSUESLabel.grid(row=3, column=0, padx=30, pady=15, sticky=W)
    ISSUEBOOKEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    ISSUEBOOKEntry.grid(row=3, column=1, pady=15, padx=10)

    RETURNBOOKLabel = Label(screen, text='Address', font=('times new roman', 20, 'bold'))
    RETURNBOOKLabel.grid(row=4, column=0, padx=30, pady=15)
    RETURNBOOKEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    RETURNBOOKEntry.grid(row=4, column=1, pady=15, padx=10)

    SEARCHBOOKLabel = Label(screen, text='Gender', font=('times new roman', 20, 'bold'))
    SEARCHBOOKLabel.grid(row=5, column=0, padx=30, pady=15)
    SEARCHBOOKEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    SEARCHBOOKEntry.grid(row=5, column=1, pady=15, padx=10)

    Library_button = ttk.Button(screen, text=button_text, command=command)
    Library_button.grid(row=7, columnspan=2, pady=15)




def view_library():
    query = 'select * from Library'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    LibraryTable.delete(*LibraryTable.get_children())
    for data in fetched_data:
        LibraryTable.insert('', END, values=data)


def delete_student():
    indexing=LibraryTable.focus()
    print(indexing)
    content=LibraryTable.item(indexing)
    content_id=content['values'][0]
    query='delete from Library where ADDBOOK=%s'
    mycursor.execute(query,content_id)
    con.commit()
    messagebox.showinfo('Deleted',f'Id {content_id} is deleted successfully')
    query='select * from Library'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    LibraryTable.delete(*LibraryTable.get_children())
    for data in fetched_data:
        LibraryTable.insert('',END,values=data)






def search_data():
    query='SELECT * from Library where ADDBOOK=%s or VIEWBOOK=%s or ISSUEBOOK=%s or RETURNBOOK=%s or SEARCHBOOK=%s'
    mycursor.execute(query,(ADDBOOKEntry.get(),VIEWBOOKEntry.get(),ISSUEBOOKEntry.get(),RETURNBOOKEntry.get(),SEARCHBOOKEntry.get()))
    LibraryTable.delete(*LibraryTable.get_children())
    fetched_data=mycursor.fetchall()
    for data in fetched_data:
        LibraryTable.insert('',END,values=data)




def add_data():
    if ADDBOOKEntry.get()=='' or VIEWBOOKEntry.get()=='' or ISSUEBOOKEntry.get()=='' or RETURNBOOKEntry.get()=='' or SEARCHBOOKEntry.get()=='' :
        messagebox.showerror('Error','All Feilds are Reuqired',parent=screen)
    else:


        try:
            query = 'insert into student values(%s,%s,%s,%s,%s)'
            mycursor.execute(query, (
            ADDBOOKEntry.get(), VIEWBOOKEntry.get(), ISSUEBOOKEntry.get(), RETURNBOOKEntry.get(), SEARCHBOOKEntry.get(),date, currenttime))
            con.commit()
            result = messagebox.askyesno('Confirm', 'Data added successfully.Do you want clean the form?',
                                         parent=screen)
            if result:
                ADDBOOKEntry.delete(0, END)
                VIEWBOOKEntry.delete(0, END)
                ISSUEBOOKEntry.delete(0, END)
                RETURNBOOKEntry.delete(0, END)
                SEARCHBOOKEntry.delete(0, END)
                #genderEntry.delete(0, END)
                #dobEntry.delete(0, END)
            else:
                pass
        except:
            messagebox.showerror('Error','Id cannot be repeated',parent=screen)
            return

        query='select * from Library'
        mycursor.execute(query)
        fetched_data=mycursor.fetchall()
        LibraryTable.delete(*LibraryTable.get_children())
        for data in fetched_data:

            LibraryTable.insert('',END,values=data)




def connect_database():
    def connect():
        global mycursor,con

        try:
            con = pymysql.connect(host='localhost', user='root', password='1234')
            mycursor = con.cursor()
            messagebox.showinfo('Success', 'Database Connection is Successful', parent=connectWindow)


        except:
            messagebox.showerror('Error','Invalid Details',parent=connectWindow)
            return


        try:
            query = 'create database  LibraryManagementSystem'
            mycursor.execute(query)
            query='use LibraryManagementSystem '
            mycursor.execute(query)
            query='create table Library(ADD BOOK varchar(30),VIEW BOOK varchar(10),ISSUE BOOK varchar(30),RETURN BOOK varchar(100),SEARCH BOOK varchar(20))'
            mycursor.execute(query)
        except:
            query='use LibraryManagementSystem'
            mycursor.execute(query)
            messagebox.showinfo('Success','Database Connection is Successful',parent=connectWindow)
            connectWindow.destroy()

            ADDBOOKButton.config(state=NORMAL)
            VIEWBOOKButton.config(state=NORMAL)
            ISSUEBOOKButton.config(state=NORMAL)
            RETURNBOOKButton.config(state=NORMAL)
            SEARCHBOOKButton.config(state=NORMAL)
            #deletestudentButton.config(state=NORMAL)
            #addstudentButton.config(state=NORMAL)
            #addstudentButton.config(state=NORMAL)


    connectWindow=Toplevel()
    connectWindow.grab_set()
    connectWindow.geometry('470x250+730+230')
    connectWindow.title('Database Connection')
    connectWindow.resizable(0,0)

    hostnameLabel=Label(connectWindow,text='Host Name',font=('arial',20,'bold'))
    hostnameLabel.grid(row=0,column=0,padx=20)

    hostEntry=Entry(connectWindow,font=('roman',15,'bold'),bd=2)
    hostEntry.grid(row=0,column=1,padx=40,pady=20)

    usernameLabel=Label(connectWindow,text='User Name',font=('arial',20,'bold'))
    usernameLabel.grid(row=1,column=0,padx=20)

    usernameEntry=Entry(connectWindow,font=('roman',15,'bold'),bd=2)
    usernameEntry.grid(row=1,column=1,padx=40,pady=20)

    passwordLabel=Label(connectWindow,text='Password',font=('arial',20,'bold'))
    passwordLabel.grid(row=2,column=0,padx=20)

    passwordEntry=Entry(connectWindow,font=('roman',15,'bold'),bd=2)
    passwordEntry.grid(row=2,column=1,padx=40,pady=20)

    connectButton=ttk.Button(connectWindow,text='CONNECT',command=connect)
    connectButton.grid(row=3,columnspan=2)


   # count=0
    #text=''

# Global slider text variables
count = 0
text = ''
S = 'Library Management System'

def slider():
    global text, count
    if count == len(S):
        count = 0
        text = ''
    text = text + S[count]
    sliderLabel.config(text=text)
    count += 1
    sliderLabel.after(300, slider)


def clock():
    global date,currenttime
    date=time.strftime('%d/%m/%Y')
    currenttime=time.strftime('%H:%M:%S')
    datetimeLabel.config(text=f'   Date:{date}\nTime:{currenttime}')
    datetimeLabel.after(1000,clock)



#GUIpart
root=ttkthemes.ThemedTk()
root.get_themes()

root.set_theme('radiance')

root.geometry('1174x680+0+0')
root.resizable(0,0)


root.title('Library Management System') #s[count]=t when count is 1

datetimeLabel=Label(root,font=('times new roman',18,'bold'))
datetimeLabel.place(x=5,y=5)
clock()
S='Library Management System'
sliderLabel=Label(root,text=S,font=('arial',28,'italic bold'),width=30)
sliderLabel.place(x=200,y=0)
slider()

connectButton=ttk.Button(root,text='connect database',command=connect_database)
connectButton.place(x=980,y=0)

#leftFrame

leftFrame=Frame(root)
leftFrame.place(x=50,y=80,width=300,height=600)

logo_image=PhotoImage(file='student_logo.png')
logo_Label=Label(leftFrame,image=logo_image)
logo_Label.grid(row=0,column=0)

#Buttons
ADDBOOKButton=ttk.Button(leftFrame,text='ADD BOOK',width=25,state=DISABLED,command=lambda: toplevel_data('ADD BOOK', 'Add', add_data))
ADDBOOKButton.grid(row=1,column=0,pady=20)

VIEWBOOKButton=ttk.Button(leftFrame,text='VIEW BOOK',width=25,state=DISABLED)
VIEWBOOKButton.grid(row=2,column=0,pady=20)

ISSUEBOOKButton=ttk.Button(leftFrame,text='ISSUE BOOK',width=25,state=DISABLED,command=delete_student)
ISSUEBOOKButton.grid(row=3,column=0,pady=20)

RETURNBOOKButton=ttk.Button(leftFrame,text='RETURN BOOK',width=25,state=DISABLED,command=lambda: toplevel_data('RETURN BOOK', 'update', update_data))
RETURNBOOKButton.grid(row=4,column=0,pady=20)

SEARCHBOOKButton=ttk.Button(leftFrame,text='SEARCH BOOK',width=25,state=DISABLED,command=lambda: toplevel_data('SEARCH BOOK', 'update', search_data))
SEARCHBOOKButton.grid(row=5,column=0,pady=20)

exportlibraryButton=ttk.Button(leftFrame,text='Export Data',width=25,state=DISABLED,command=export_data)
exportlibraryButton.grid(row=6,column=0,pady=20)

exitButton=ttk.Button(leftFrame,text='Exit',width=25,command=exit_data)
exitButton.grid(row=7,column=0,pady=20)



#RightFrame

rightFrame=Frame(root)
rightFrame.place(x=350,y=80,width=820,height=600)

scrollBarX=Scrollbar(rightFrame,orient=HORIZONTAL)
scrollBarY=Scrollbar(rightFrame,orient=VERTICAL)


LibraryTable=ttk.Treeview(rightFrame,columns=('ADD BOOK','VIEW BOOK','ISSUE BOOK','RETURN BOOK','SEARCH BOOK'),
                          xscrollcommand=scrollBarX.set,yscrollcommand=scrollBarY.set)

scrollBarX.config(command=LibraryTable.xview)
scrollBarY.config(command=LibraryTable.yview)



scrollBarX.pack(side=BOTTOM,fill=X)
scrollBarY.pack(side=RIGHT,fill=Y)

LibraryTable.pack(fill=BOTH,expand=1)

LibraryTable.heading('ADD BOOK',text='ADD BOOK')
LibraryTable.heading('VIEW BOOK',text='VIEW BOOK')
LibraryTable.heading('ISSUE BOOK',text='ISSUE BOOK')
LibraryTable.heading('RETURN BOOK',text='RETURN BOOK')
LibraryTable.heading('SEARCH BOOK',text='SEARCH BOOK')




LibraryTable.column('ADD BOOK',width=50,anchor=CENTER)
LibraryTable.column('VIEW BOOK',width=300,anchor=CENTER)
LibraryTable.column('ISSUE BOOK',width=200,anchor=CENTER)
LibraryTable.column('RETURN BOOK',width=300,anchor=CENTER)
LibraryTable.column('SEARCH BOOK',width=300,anchor=CENTER)
#LibraryTable.column('Gender',width=100,anchor=CENTER)
#LibraryTable.column('D.O.B',width=100,anchor=CENTER)
#LibraryTable.column('Added Date',width=200,anchor=CENTER)
#LibraryTable.column('Added Time',width=200,anchor=CENTER)

Style = ttk.Style()


Style.configure('Treeview',rowheight=40,font=('arial',12,'bold'),background='white',fieldbackground='white')
Style.configure('Treeview.Heading',font=('arial',14,'bold'))


LibraryTable.config(show='headings')
root.mainloop()
"""






