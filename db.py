import tkinter
import sqlite3
from tkinter import messagebox
import sys

def validate_login():

    attempts = 0 

    #creating db
    db = sqlite3.connect("login.sqlite")
    db.execute("DROP TABLE IF EXISTS login")
    db.execute("CREATE TABLE IF NOT EXISTS login(playerID INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)") # query
    db.execute("INSERT INTO login(username, password) VALUES('player1', '123')")
    # db.execute("DELETE FROM login WHERE username='admin'")
    cursor = db.cursor() # retrieving record
    cursor.execute("SELECT * FROM login where username=? AND password=?", (user_input.get(), pass_input.get()))
#    count_records = cursor.fetchone().execute("SELECT COUNT(*) FROM login")

    row = cursor.fetchone() # return each row in db
    while attempts < 3:
        if row: # as cursor.fetchone() iterates, this will check if the next row is empty
            messagebox.showinfo("info", "Login successful")
            
        else:
            messagebox.showinfo("info", "Login failed")
            attempts += 1
            print(attempts)
        if attempts == 3:
            break
    sys.exit()

        
        
    cursor.connection.commit() # saving changes to db
    db.close() # closing db
    


main_window = tkinter.Tk()
main_window.title("Login Form")
main_window.geometry("400x300")
pad = 20
main_window["padx"] = pad
user_input = tkinter.StringVar()
pass_input = tkinter.StringVar()
info_label = tkinter.Label(main_window, text= "Login Application")
info_label.grid(row=0, column=0, pady = 20)

#username
info_user  = tkinter.Label(main_window, text= "Username: ")
info_user.grid(row=1, column=0, pady = 20)
userinput = tkinter.Entry(main_window, textvariable=user_input)
userinput.grid(row=1, column= 1)

# password
info_pass  = tkinter.Label(main_window, text= "Password: ")
info_pass.grid(row=2, column=0, pady = 20)
passinput = tkinter.Entry(main_window, textvariable=pass_input, show = "*")
passinput.grid(row=2, column= 1)

login_btn = tkinter.Button(main_window, text =  "Login", command = validate_login)

login_btn.grid(row=3, column=1)


main_window.mainloop()





