#Question 1
#this program converts roman numerals to ordinary numerals
class Solution:
    def romanToNum(self,s: str) -> int:
        num=(("M", 1000), ("CM", 900), ("D", 500), ("CD", 400), ("C", 100), ("XC", 90), ("L", 50), ("XL", 40), ("X", 10), ("IX", 9), ("V", 5), ("IV", 4), ("I", 1),
        ("m", 1000), ("cm", 900), ("d", 500), ("cd", 400), ("c", 100), ("xc", 90), ("l", 50), ("xl", 40), ("x", 10), ("ix", 9), ("v", 5), ("iv", 4), ("i", 1))
        ans = 0

        for i in range(len(s)):
            if i+1 != len(s) and num[s[i]]<num[s[i+1]]:
                ans = ans - [s[i]]
                return ans
                choice1 = input1("Enter a roman numeral to convert: ")
                return ans   
                choice2 = input2("Do you want to repeat(Y/N)?: ")
                choice2a = Y
                choice2b = N
def input2(self):
    self.input2 = input2
def input1(self):
    self.input1 = input1
def choice2a(self):
    self.choice2a = "Y"
def choice2b(self):
    self.choice2b = "N"    
if input2 == choice2a:
    print(input1)
elif input2 == choice2b:
    exit() 

#Question 2
#this program simulates an ATM
import imp
import random
from re import search
import sqlite3
import time
from tkinter import END, Button, Label, messagebox

class Account:
    def __init__(self, id, Balance = 0):
        self.id = id
        self.Balance = Balance
    
    def getId(self):
        return self.id
    
    def AccountBalance(self):
        return self.Balance
    
    def withdrawAccount(self, amount)
        self.Balance += amount

def main():
    accounts = []
    for i in range(1000, 9999):
        account = Account(i, 0)
        accounts.append(account)

while True:
    print("---------ATM SYSTEM---------")
    user = str(input("\nEnter User Name: "))

    id = int(input("\nPlease Enter Pin: "))
    while id <1000 or id > 9999:
        id = int =(input("\nInvalid Pin...Re-Enter: "))

        while True:
            print("\nOptions: ")
            print("""\n1 - Make a Deposit \t\n2 - Make a Withdrawal \n3 - Obtain Balance \t\t\n4 - Change Pin \n5 - Quit""")

            selection = int(input("\nMake a selection from the options menu: "))

            for acc in accounts:
                if acc.getID() == id:
                    accountObj = acc
                    break
            
            if selection == 1:
                amt = float(input("\nEnter amount to Deposit: "))
                ver_deposit = input(f"Is R{format(amt, '2f')} the correct amount you want to Deposir, Yes or No ? ")
                ver_deposit = ver_deposit.upper()

                if ver_deposit == "YES":
                    print("\nVerified checking account deposit")
                    time.sleep(2)
                    accountObj.depositAccount(amt)
                    print(f"\nYour New Balance Is: R{format(accountObj.AccountBalance(), '2f')} ")
                    time.sleep(2)
                else:
                    break
            
            elif selection == 2:
                amt = float(input("\nEnter Amount to Withdraw: "))
                ver_withdraw = input(f"Is R{format(amt, '2f')} the correct amount to withdraw, Yes or No ?")
                ver_withdraw = ver_withdraw.upper()
                if ver_withdraw == "YES":
                    print("\nVerified account withdraw.")
                    time.sleep(2)
                else:
                    break
                if amt < accountObj.AccountBalance():
                    accountObj.withdrawAccount(amt)
                    print(f"\nYour New Balance Is: R{format(accountObj.AccountBalance(), '2f')} ")
                    time.sleep(2)
                else:
                    print(f"\nYour checking account balance is less than withdrawal amount: R{format(accountObj.AccountBalance(), '2f')}")
                time.sleep(2)
            
            elif selection == 3:
                print(f"\nObtain Balance: R{format(accountObj.AccountBalance(), '2f')}")
                time.sleep(2)
            
            elif selection == 4:
                print(f"\nChange Pin")
                id = int(input("\nEnter a new pin"))
                id = int(input("\nConfirm new pin"))
                while id < 1000 or id > 9999:
                    id = int(input("\nNew pin saved: "))
            
            elif selection == 5:
                exit()

#Question 3

from tkinter import *
from tkinter import messagebox
import sqlite3

root = Tk()
root.title("Student Enquiry System")
root.geometry("700x500")

def define_layout():

    def create_DB():
        connect = sqlite3.connect("enquiry_database.db")

        sqlite3.Cursor = sqlite3.connect.cursor()

        statement = """"CREATE A TABLE IF NOT EXISTS tbl_Enquiries(
        Query_ID INTEGER PRIMARY KEY,
        Name TEXT,
        Surname TEXT,
        Email TEXT,
        Query TEXT,
        )"""

        sqlite3.Cursor.execute(statement)

        #Automates Query ID number
        sqlite3.Cursor.execute("SELECT * FROM tbl_Enquiries")
        num_records = sqlite3.Cursor.fetchall()
        print(len(num_records))
        insert_query = f"INSERT INTO tbl_Enquiries VALUES ({1 + len(num_records)}, '{name_textbox.get()}' ,"\
                       f"'{surname_textbox.get()}', '{email_textbox.get()}', '{sq_textbox.get()}')"
sqlite3.Cursor.execute(insert_query)

sqlite3.connect.commit()

sqlite3.connect.close()

messagebox.showinfo("Notification" , "Submitted!")
name_textbox.delete(0, END)
surname_textbox.delete(0, END)
email_textbox.delete(0, END)
sq_textbox.delete(0, END)

def display_data():
    connect = sqlite3.connect("enquiry_database.db")

    sqlite3.Cursor = sqlite3.connect.cursor()
    sqlite3.Cursor.execute("SELECT * FROM tbl_Enquiries")
    all_records = cursor.fetchall()
    print(len(all_records))
    print(all_records)

def define_layout():
    display_records = ""
    for i in all_records:
        display_records += str(i) + "/n"
    
    print(display_records)

    queries_label = Label(root, text=display_records)
    queries_label.grid(row=0, coloumn=3)

    sqlite3.connect.commit()
    sqlite3.connect.close()

def clear():
    null = ""
    display_records = ""

    for i in null:
        display_records += str(i) + "\n"

    queries_label = Label(root, text=display_records)
    queries_label.grid(row=0, coloumn=3)

    print(display_records)

def delete():
    sqlite3.connect = sqlite3.connect("enquiry_database.db")

    sqlite3.Cursor = sqlite3.connect.cursor()
    sqlite3.Cursor.execute(f'DELETE FROM tbl_Enquiries WHERE Query_ID ={delete_textbox.get()}')

    print("Deletion Complete")

    sqlite3.connect.commit()

    sqlite3.connect.close()

    messagebox.showinfo("Notification", "Deleted!")
    delete_textbox.delete(0, END)
    pass

def search_name():
    sqlite3.connect = sqlite3.connect("enquiry_database.db")

    cursor = connect.cursor()
    cursor.execute(f"SELECT * FROM tbl_Enquiries WHERE Name='{search_textbox.get}'")
    search = sqlite3.Cursor.fetchall()

    display_records = ""
    for i in search:
        display_records += str(i) + "\n"
    print(f"Result: {display_records}")

    if display_records == "":
        messagebox.showinfo("Notification", "Name does not exist!")
        queries_label = Label(root, text=display_records)
        queries_label.grid(row=0, coloumn=3)
    else:
        queries_label = Label(root, text=display_records)
        queries_label.grid(row=0, coloumn=3)

name_label = Label(root, text="Name")
name_textbox = Entry(root)
name_label.grid(row=0, coloumn=0)
name_textbox.grid(row=1, coloumn=0)

surname_label = Label(root, text="Surname")
surname_textbox = Entry(root)
surname_label.grid(row=3, coloumn=0)
surname_textbox.grid(row=4, coloumn=0)

email_label = Label(root, text="Email")
email_textbox = Entry(root)
email_label.grid(row=6, coloumn=0)
email_textbox.grid(row=7, coloumn=0)

sq_label = Label(root, text="Student Query")
sq_textbox = Entry(root)
sq_label.grid(row=9, coloumn=0)
sq_textbox.grid(row=10, coloumn=0)

submit_button = Button(root, text="Submit", command=logquery)
submit_button.grid(row=12, coloumn=0, pady=(10, 0))

search_label = Label(root, text="Enter Name to Search")
search_textbox = Entry(root)
search.button = Button(root, text="Search", command=search_name)
search_label.grid(row=14, coloumn=0)
search_textbox.grid(row=15, coloumn=0)
search_button.grid(row=16, coloumn=0)
