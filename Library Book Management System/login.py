from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk


def login():
    if usernameEntry.get() == '' or passwordEntry.get() == '':
        messagebox.showerror('Error', 'Fields cannot be empty', parent=window)
    elif usernameEntry.get() == 'Bhoomika' and passwordEntry.get() == '1234':
        messagebox.showinfo('Success', 'Login Successful', parent=window)
        window.destroy()
        import lib  # Import AFTER destroying the login window
    else:
        messagebox.showerror('Error', 'Invalid username or password', parent=window)

# Main window setup
window = Tk()
window.geometry('1280x700+0+0')
window.title('Login System of Student Management System')
window.resizable(0, 0)


# Background
bg_img = Image.open('bglb.jpg')
window.backgroundImage = ImageTk.PhotoImage(bg_img)
bgLabel = Label(window, image=window.backgroundImage)
bgLabel.place(x=0, y=0)


# Login frame
loginFrame = Frame(window, bg='white')
loginFrame.place(x=400, y=150)

window.logoImage = PhotoImage(file='loginlb.png')
logoLabel = Label(loginFrame, image=window.logoImage)
logoLabel.grid(row=0, column=0, columnspan=2, pady=10)

window.usernameImage = PhotoImage(file='userlb.png')
usernameLabel= Label(loginFrame, image=window.usernameImage, text='Username', compound=LEFT,
                      font=('times new roman', 20, 'bold'), bg='white')
usernameLabel.grid(row=1, column=0, pady=10, padx=20)

usernameEntry = Entry(loginFrame, font=('times new roman', 20, 'bold'), bd=5, fg='royalblue')
usernameEntry.grid(row=1, column=1, pady=10, padx=20)

window.passwordImage = PhotoImage(file='passlb.png')
passwordLabel = Label(loginFrame, image=window.passwordImage, text='Password', compound=LEFT,
                      font=('times new roman', 20, 'bold'), bg='white')
passwordLabel.grid(row=2, column=0, pady=10, padx=20)

passwordEntry = Entry(loginFrame, font=('times new roman', 20, 'bold'), bd=5, fg='royalblue', show='*')
passwordEntry.grid(row=2, column=1, pady=10, padx=20)

loginButton = Button(loginFrame, text='Login', font=('times new roman', 14, 'bold'), width=15, fg='white',
                     bg='cornflowerblue', activebackground='cornflowerblue', activeforeground='white',
                     cursor='hand2', command=login)
loginButton.grid(row=3, column=1, pady=10)

window.mainloop()
