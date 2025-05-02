# -Library-Management-System
A Python-based Library Management System with a graphical user interface built using Tkinter and MySQL for database management. This project is designed to help manage books efficiently by allowing users to add, search, issue, return, and view book records with ease.

✨ Features
Add new books to the library

Search for books by ID or name

View all available books

Issue books to students

Return books and update status

Delete outdated or unwanted book records

User-friendly GUI interface

Backend powered by MySQL database

🛠️ Technologies Used
Python (Tkinter for GUI)

MySQL (Database)

Pymysql or MySQL Connector (for DB connectivity)

📁 Project Structure


Library-Management-System/
│
├── main.py               # Main application script
├── db_config.py          # Database configuration
├── add_book.py           # Module for adding books
├── view_books.py         # Module to view books
├── issue_book.py         # Module to issue books
├── return_book.py        # Module to return books
├── search_book.py        # Module to search books
├── delete_book.py        # Module to delete books
└── README.md             # Project description
⚙️ Setup Instructions
Clone the repository:


git clone (https://github.com/Bhoomika9019)/BHOOMIKA B P/Library-Management-System.git
Set up your MySQL database and update the credentials in db_config.py.

Install required Python packages:

pip install pymysql
Run the application:

python main.py

📌 Note
Ensure MySQL service is running before launching the application.
