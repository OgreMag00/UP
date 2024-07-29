import customtkinter as ctk
import test_page, textbook_page
import config


def get_test(frame, master):
    frame.destroy()
    test_page.testpage(master=master)

def get_textbook(frame, master):
    frame.destroy()
    textbook_page.textbookpage(master=master)

def mainpage(master):
    frame = ctk.CTkFrame(master=master, fg_color='transparent', width=700, height=700)
    frame.grid(row=0, column=0)
    
    logo = ctk.CTkLabel(master=frame, text='menu', width=200, font=('Arial', 120))
    logo.grid(row=0, column=0)

    but_textbook = ctk.CTkButton(master=frame, text='textbook', command= lambda: get_textbook(frame, master), font=('Arial', 70), fg_color=config.button_color)
    but_textbook.grid(row=1, column=0, pady=20, sticky="ew")

    but_test = ctk.CTkButton(master=frame, text='test', command= lambda: get_test(frame, master), font=('Arial', 70), fg_color=config.button_color)
    but_test.grid(row=2, column=0, pady=10, sticky="ew")

