# Library Management System using Tkinter and MySQL

from tkinter import *
import time
import ttkthemes
from tkinter import ttk, messagebox, filedialog
import pymysql
import pandas

# Functionality

def exit_app():
    result = messagebox.askyesno('Confirm', 'Do you want to exit?')
    if result:
        root.destroy()


def export_data():
    url = filedialog.asksaveasfilename(defaultextension='.csv')
    indexing = bookTable.get_children()
    newlist = []
    for index in indexing:
        content = bookTable.item(index)
        datalist = content['values']
        newlist.append(datalist)

    table = pandas.DataFrame(newlist, columns=['Book ID', 'Title', 'Author', 'Genre', 'Quantity', 'Issued', 'Added Date', 'Added Time'])
    table.to_csv(url, index=False)
    messagebox.showinfo('Success', 'Data saved successfully')


def toplevel_data(title, button_text, command):
    global bookIdEntry, titleEntry, authorEntry, genreEntry, quantityEntry, screen

    screen = Toplevel()
    screen.title(title)
    screen.grab_set()
    screen.resizable(0, 0)

    Label(screen, text='Book ID', font=('times new roman', 20, 'bold')).grid(row=0, column=0, padx=30, pady=15, sticky=W)
    bookIdEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    bookIdEntry.grid(row=0, column=1, pady=15, padx=10)

    Label(screen, text='Title', font=('times new roman', 20, 'bold')).grid(row=1, column=0, padx=30, pady=15, sticky=W)
    titleEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    titleEntry.grid(row=1, column=1, pady=15, padx=10)

    Label(screen, text='Author', font=('times new roman', 20, 'bold')).grid(row=2, column=0, padx=30, pady=15, sticky=W)
    authorEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    authorEntry.grid(row=2, column=1, pady=15, padx=10)

    Label(screen, text='Genre', font=('times new roman', 20, 'bold')).grid(row=3, column=0, padx=30, pady=15, sticky=W)
    genreEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    genreEntry.grid(row=3, column=1, pady=15, padx=10)

    Label(screen, text='Quantity', font=('times new roman', 20, 'bold')).grid(row=4, column=0, padx=30, pady=15, sticky=W)
    quantityEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    quantityEntry.grid(row=4, column=1, pady=15, padx=10)

    ttk.Button(screen, text=button_text, command=command).grid(row=5, columnspan=2, pady=15)


def add_book():
    if bookIdEntry.get() == '' or titleEntry.get() == '' or authorEntry.get() == '' or genreEntry.get() == '' or quantityEntry.get() == '':
        messagebox.showerror('Error', 'All fields are required', parent=screen)
        return

    try:
        query = 'INSERT INTO books VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
        mycursor.execute(query, (bookIdEntry.get(), titleEntry.get(), authorEntry.get(), genreEntry.get(), quantityEntry.get(), 0, date, currenttime))
        con.commit()
        messagebox.showinfo('Success', 'Book added successfully', parent=screen)
        screen.destroy()
        show_books()
    except:
        messagebox.showerror('Error', 'Book ID must be unique', parent=screen)


def show_books():
    query = 'SELECT * FROM books'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    bookTable.delete(*bookTable.get_children())
    for data in fetched_data:
        bookTable.insert('', END, values=data)


def search_book():
    query = 'SELECT * FROM books WHERE book_id=%s OR title=%s OR author=%s OR genre=%s'
    mycursor.execute(query, (bookIdEntry.get(), titleEntry.get(), authorEntry.get(), genreEntry.get()))
    bookTable.delete(*bookTable.get_children())
    fetched_data = mycursor.fetchall()
    for data in fetched_data:
        bookTable.insert('', END, values=data)


def issue_book():
    indexing = bookTable.focus()
    content = bookTable.item(indexing)
    book_id = content['values'][0]
    query = 'UPDATE books SET issued = issued + 1 WHERE book_id = %s'
    mycursor.execute(query, (book_id,))
    con.commit()
    messagebox.showinfo('Success', f'Book {book_id} issued successfully')
    show_books()


def return_book():
    indexing = bookTable.focus()
    content = bookTable.item(indexing)
    book_id = content['values'][0]
    query = 'UPDATE books SET issued = issued - 1 WHERE book_id = %s AND issued > 0'
    mycursor.execute(query, (book_id,))
    con.commit()
    messagebox.showinfo('Success', f'Book {book_id} returned successfully')
    show_books()


def connect_database():
    def connect():
        global mycursor, con

        try:
            con = pymysql.connect(host='localhost', user='root', password='1234')
            mycursor = con.cursor()
            mycursor.execute('CREATE DATABASE IF NOT EXISTS LibraryManagement')
            mycursor.execute('USE LibraryManagement')
            mycursor.execute('''CREATE TABLE IF NOT EXISTS books (
                book_id INT PRIMARY KEY,
                title VARCHAR(100),
                author VARCHAR(100),
                genre VARCHAR(50),
                quantity INT,
                issued INT,
                added_date VARCHAR(50),
                added_time VARCHAR(50))''')
            messagebox.showinfo('Success', 'Database connected successfully', parent=connectWindow)
            connectWindow.destroy()
            enable_buttons()
        except Exception as e:
            messagebox.showerror('Error', f'{e}', parent=connectWindow)

    connectWindow = Toplevel()
    connectWindow.grab_set()
    connectWindow.geometry('470x250+730+230')
    connectWindow.title('Database Connection')
    connectWindow.resizable(0, 0)

    Label(connectWindow, text='Host Name', font=('arial', 20, 'bold')).grid(row=0, column=0, padx=20)
    hostEntry = Entry(connectWindow, font=('roman', 15, 'bold'))
    hostEntry.grid(row=0, column=1, padx=40, pady=20)

    Label(connectWindow, text='User Name', font=('arial', 20, 'bold')).grid(row=1, column=0, padx=20)
    usernameEntry = Entry(connectWindow, font=('roman', 15, 'bold'))
    usernameEntry.grid(row=1, column=1, padx=40, pady=20)

    Label(connectWindow, text='Password', font=('arial', 20, 'bold')).grid(row=2, column=0, padx=20)
    passwordEntry = Entry(connectWindow, font=('roman', 15, 'bold'), show='*')
    passwordEntry.grid(row=2, column=1, padx=40, pady=20)

    ttk.Button(connectWindow, text='CONNECT', command=connect).grid(row=3, columnspan=2)


def enable_buttons():
    addBookButton.config(state=NORMAL)
    searchBookButton.config(state=NORMAL)
    issueBookButton.config(state=NORMAL)
    returnBookButton.config(state=NORMAL)
    showBookButton.config(state=NORMAL)
    exportBookButton.config(state=NORMAL)


def slider():
    global text, count
    if count == len(s):
        count = 0
        text = ''
    text += s[count]
    sliderLabel.config(text=text)
    count += 1
    sliderLabel.after(300, slider)


def clock():
    global date, currenttime
    date = time.strftime('%d/%m/%Y')
    currenttime = time.strftime('%H:%M:%S')
    datetimeLabel.config(text=f'Date: {date}\nTime: {currenttime}')
    datetimeLabel.after(1000, clock)


# GUI
root = ttkthemes.ThemedTk()
root.get_themes()
root.set_theme('radiance')
root.geometry('1174x680+0+0')
root.resizable(0, 0)
root.title('Library Management System')

count = 0
text = ''
s = 'Library Management System'

sliderLabel = Label(root, text=s, font=('arial', 28, 'italic bold'), width=30)
sliderLabel.place(x=200, y=0)
slider()

datetimeLabel = Label(root, font=('times new roman', 18, 'bold'))
datetimeLabel.place(x=5, y=5)
clock()

connectButton = ttk.Button(root, text='Connect Database', command=connect_database)
connectButton.place(x=980, y=0)

# Left Frame
leftFrame = Frame(root)
leftFrame.place(x=50, y=80, width=300, height=600)

addBookButton = ttk.Button(leftFrame, text='Add Book', width=25, state=DISABLED, command=lambda: toplevel_data('Add Book', 'Add', add_book))
addBookButton.grid(row=1, column=0, pady=20)

searchBookButton = ttk.Button(leftFrame, text='Search Book', width=25, state=DISABLED, command=lambda: toplevel_data('Search Book', 'Search', search_book))
searchBookButton.grid(row=2, column=0, pady=20)

issueBookButton = ttk.Button(leftFrame, text='Issue Book', width=25, state=DISABLED, command=issue_book)
issueBookButton.grid(row=3, column=0, pady=20)

returnBookButton = ttk.Button(leftFrame, text='Return Book', width=25, state=DISABLED, command=return_book)
returnBookButton.grid(row=4, column=0, pady=20)

showBookButton = ttk.Button(leftFrame, text='View Books', width=25, state=DISABLED, command=show_books)
showBookButton.grid(row=5, column=0, pady=20)

exportBookButton = ttk.Button(leftFrame, text='Export Data', width=25, state=DISABLED, command=export_data)
exportBookButton.grid(row=6, column=0, pady=20)

exitButton = ttk.Button(leftFrame, text='Exit', width=25, command=exit_app)
exitButton.grid(row=7, column=0, pady=20)

# Right Frame
rightFrame = Frame(root)
rightFrame.place(x=350, y=80, width=820, height=600)

scrollBarX = Scrollbar(rightFrame, orient=HORIZONTAL)
scrollBarY = Scrollbar(rightFrame, orient=VERTICAL)

bookTable = ttk.Treeview(rightFrame, columns=('Book ID', 'Title', 'Author', 'Genre', 'Quantity', 'Issued', 'Added Date', 'Added Time'),
                         xscrollcommand=scrollBarX.set, yscrollcommand=scrollBarY.set)
scrollBarX.config(command=bookTable.xview)
scrollBarY.config(command=bookTable.yview)

scrollBarX.pack(side=BOTTOM, fill=X)
scrollBarY.pack(side=RIGHT, fill=Y)
bookTable.pack(fill=BOTH, expand=1)

for col in ('Book ID', 'Title', 'Author', 'Genre', 'Quantity', 'Issued', 'Added Date', 'Added Time'):
    bookTable.heading(col, text=col)
    bookTable.column(col, anchor=CENTER)

bookTable.config(show='headings')
Style = ttk.Style()
Style.configure('Treeview', rowheight=40, font=('arial', 12, 'bold'))
Style.configure('Treeview.Heading', font=('arial', 14, 'bold'))

root.mainloop()
