import os
import tkinter
import tkinter as tk
from tkinter.ttk import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time


def sec():
    


    # Email and password (for app-specific passwords or OAuth in production)
    sender_email = "pushmail817@gmail.com"
    password = "ybvv ucss zgcv ewev"  # Use App Passwords if 2FA is enabled
    receiver_email = "nishanthan.v2006@gmail.com"

    # Create the email message
    subject = "Test Email from Python"
    body = "PH VALUE IS 6"

    # Set up the MIME
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Attach the body to the email
    message.attach(MIMEText(body, "plain"))

    # Send the email
    try:
        # Set up the server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()  # Secure the connection
        server.login(sender_email, password)  # Corrected this line

        # Send the email
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully!")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        server.quit()


    
def count():
        n=0
        while(n<10):
            time.sleep(1)
            n=n+1
            print(n)
            if n==6:
                sec()

def main():
    
    main_window = tkinter.Tk()
    main_window.geometry("1366x768")
    main_window.title('Login Page')  #title
    main_window.resizable(0,0)
    main_window.configure(bg="#12232E")
    a = Canvas(main_window,width=900,height=500,bg="#3F6BAA")
    a.create_rectangle(0, 0, 0, 0, fill="#3F6BAA")
    a.place(relx = 0.5,rely = 0.5,anchor=tkinter.CENTER)
        
    Button1 = tkinter.Button(main_window,text = "CHECK PH VALUE",command =count,fg = "white", font="Bahnschrift", bg = "pale green4", height=1,width= 20)    #enter button
    Button1.place(relx = 0.4,rely = 0.5, anchor = tkinter.W)
    main_window.mainloop()

   
main()

